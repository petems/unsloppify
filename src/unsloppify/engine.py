"""Rule loading, prose segmentation, and finding emission."""

from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass, field
from importlib import resources
from pathlib import Path

import yaml

SEVERITY_ORDER = {"info": 0, "warning": 1, "error": 2}

# Fenced code blocks (``` or ~~~) and inline code spans must not be scanned.
# We collect their spans first, then scan only the gaps.
_FENCE_RE = re.compile(
    r"(?ms)^(?P<fence>`{3,}|~{3,}).*?^(?P=fence)\s*$",
)
_INLINE_CODE_RE = re.compile(r"`+[^`\n]+?`+")
# Front-matter (YAML at top of file) — skip too.
_FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
# Indented code blocks: a 4-space-indented line right after a blank line.
# Cheap heuristic: skip any line that starts with 4+ spaces or a tab when
# the previous line was blank. We handle that during segmentation.


@dataclass(frozen=True)
class Rule:
    id: str
    category: str
    severity: str
    pattern: str
    message: str
    fixable: bool = False
    replacement: str | None = None
    case_sensitive: bool = False
    word_boundary: bool = False
    examples: list[str] = field(default_factory=list)

    def compile(self) -> re.Pattern[str]:
        flags = 0 if self.case_sensitive else re.IGNORECASE
        pat = self.pattern
        if self.word_boundary:
            pat = rf"\b(?:{pat})\b"
        return re.compile(pat, flags)


@dataclass(frozen=True)
class Finding:
    file: Path
    line: int
    column: int
    end_line: int
    end_column: int
    rule_id: str
    category: str
    severity: str
    message: str
    snippet: str
    fixable: bool
    replacement: str | None

    def severity_rank(self) -> int:
        return SEVERITY_ORDER.get(self.severity, 0)


def _bundled_rule_files() -> list[Path]:
    pkg = resources.files("unsloppify").joinpath("rules")
    return sorted(Path(str(p)) for p in pkg.iterdir() if str(p).endswith(".yaml"))


def load_rules(extra_paths: list[Path] | None = None) -> list[Rule]:
    """Load all bundled rules, optionally extended with user-provided YAML files."""
    rules: list[Rule] = []
    seen_ids: set[str] = set()

    paths: list[Path] = list(_bundled_rule_files())
    if extra_paths:
        paths.extend(extra_paths)

    for path in paths:
        with open(path, encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        for raw in data.get("rules", []):
            rule = Rule(
                id=raw["id"],
                category=raw.get("category", data.get("category", "general")),
                severity=raw.get("severity", "warning"),
                pattern=raw["pattern"],
                message=raw["message"],
                fixable=raw.get("fixable", False),
                replacement=raw.get("replacement"),
                case_sensitive=raw.get("case_sensitive", False),
                word_boundary=raw.get("word_boundary", False),
                examples=list(raw.get("examples", []) or []),
            )
            if rule.id in seen_ids:
                raise ValueError(f"Duplicate rule id: {rule.id} (in {path})")
            seen_ids.add(rule.id)
            rules.append(rule)

    return rules


def _mask_skipped_regions(text: str) -> str:
    """Replace code/frontmatter regions with spaces (preserving offsets) so regex
    scanning ignores them but line/column math still maps to the original text."""

    def _spaces_for(match: re.Match[str]) -> str:
        return "".join("\n" if c == "\n" else " " for c in match.group(0))

    masked = text
    masked = _FRONTMATTER_RE.sub(_spaces_for, masked, count=1)
    masked = _FENCE_RE.sub(_spaces_for, masked)
    masked = _INLINE_CODE_RE.sub(_spaces_for, masked)
    return masked


def _line_col(text: str, offset: int) -> tuple[int, int]:
    """1-indexed line and column for a character offset."""
    prefix = text[:offset]
    line = prefix.count("\n") + 1
    last_nl = prefix.rfind("\n")
    column = offset - last_nl  # 1-indexed
    return line, column


def scan_text(text: str, rules: list[Rule], file: Path) -> Iterator[Finding]:
    """Yield findings for `text` against `rules`. Code regions are skipped."""
    masked = _mask_skipped_regions(text)
    for rule in rules:
        compiled = rule.compile()
        for m in compiled.finditer(masked):
            start, end = m.span()
            line, col = _line_col(text, start)
            end_line, end_col = _line_col(text, end)
            snippet = text[max(0, start - 20) : end + 20].replace("\n", " ")
            yield Finding(
                file=file,
                line=line,
                column=col,
                end_line=end_line,
                end_column=end_col,
                rule_id=rule.id,
                category=rule.category,
                severity=rule.severity,
                message=rule.message,
                snippet=snippet,
                fixable=rule.fixable,
                replacement=rule.replacement,
            )


def scan_file(path: Path, rules: list[Rule]) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    return list(scan_text(text, rules, path))


def iter_markdown_files(target: Path) -> Iterator[Path]:
    """Yield .md / .mdx / .markdown files under a path (recursive for dirs)."""
    if target.is_file():
        yield target
        return
    if not target.exists():
        return
    suffixes = {".md", ".mdx", ".markdown"}
    for p in target.rglob("*"):
        if p.is_file() and p.suffix.lower() in suffixes:
            yield p
