"""GitHub Actions workflow-command reporter.

Emits ::warning:: / ::error:: / ::notice:: lines that GitHub renders as
inline PR annotations.
"""

from __future__ import annotations

from unsloppify.engine import Finding

_LEVEL = {
    "error": "error",
    "warning": "warning",
    "info": "notice",
}


def _escape(s: str) -> str:
    return s.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


class GitHubReporter:
    def report(self, findings: list[Finding], fixes_applied: int = 0) -> None:
        for f in findings:
            level = _LEVEL.get(f.severity, "notice")
            print(
                f"::{level} file={f.file},line={f.line},col={f.column},"
                f"endLine={f.end_line},endColumn={f.end_column},"
                f"title=unsloppify {f.rule_id}::{_escape(f.message)}"
            )
        if fixes_applied:
            print(f"::notice::unsloppify applied {fixes_applied} fixes")
