"""Apply safe deterministic rewrites to prose, skipping code regions."""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass

from unsloppify.engine import _FENCE_RE, _FRONTMATTER_RE, _INLINE_CODE_RE, Rule


@dataclass(frozen=True)
class FixResult:
    new_text: str
    changes: int


def _protected_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for m in _FRONTMATTER_RE.finditer(text):
        spans.append(m.span())
        break  # only one front-matter, at the very top
    for m in _FENCE_RE.finditer(text):
        spans.append(m.span())
    for m in _INLINE_CODE_RE.finditer(text):
        spans.append(m.span())
    spans.sort()
    return spans


def _segments(text: str) -> list[tuple[int, int, bool]]:
    """Return list of (start, end, is_prose) covering the whole text."""
    protected = _protected_spans(text)
    out: list[tuple[int, int, bool]] = []
    cursor = 0
    for start, end in protected:
        if start > cursor:
            out.append((cursor, start, True))
        out.append((start, end, False))
        cursor = end
    if cursor < len(text):
        out.append((cursor, len(text), True))
    return out


def apply_fixes(text: str, rules: list[Rule]) -> FixResult:
    """Run fixable rules' regex substitutions on prose segments only.

    Each fixable rule must define a `replacement`; the regex's groups are
    available via standard backref syntax in the replacement.
    """
    fixable = [r for r in rules if r.fixable and r.replacement is not None]
    if not fixable:
        return FixResult(new_text=text, changes=0)

    total_changes = 0
    parts: list[str] = []
    for start, end, is_prose in _segments(text):
        segment = text[start:end]
        if is_prose:
            for rule in fixable:
                compiled = rule.compile()
                segment, n = compiled.subn(_safe_replacement(rule), segment)
                total_changes += n
        parts.append(segment)
    return FixResult(new_text="".join(parts), changes=total_changes)


def _safe_replacement(rule: Rule) -> Callable[[re.Match[str]], str]:
    """Wrap a literal replacement so backref-like sequences in user-supplied
    replacements don't blow up when the source pattern has no groups."""
    replacement = rule.replacement or ""

    def _sub(match: re.Match[str]) -> str:
        try:
            return match.expand(replacement)
        except re.error:
            return replacement

    return _sub
