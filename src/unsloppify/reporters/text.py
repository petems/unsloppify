"""Human-readable terminal reporter using rich."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.text import Text

from unsloppify.engine import Finding

_SEVERITY_STYLE = {
    "error": "bold red",
    "warning": "yellow",
    "info": "cyan",
}


class TextReporter:
    def __init__(self, console: Console | None = None) -> None:
        self.console = console or Console()

    def report(self, findings: list[Finding], fixes_applied: int = 0) -> None:
        if not findings and fixes_applied == 0:
            self.console.print("[green]clean.[/green] no findings.")
            return

        by_file: dict[Path, list[Finding]] = {}
        for f in findings:
            by_file.setdefault(f.file, []).append(f)

        for path, items in sorted(by_file.items(), key=lambda kv: str(kv[0])):
            self.console.print()
            self.console.print(f"[bold]{path}[/bold]")
            for f in items:
                tag = Text(f.severity, style=_SEVERITY_STYLE.get(f.severity, "white"))
                loc = Text(f"{f.line}:{f.column}", style="dim")
                rule = Text(f.rule_id, style="dim")
                fixable = Text(" [fixable]", style="green") if f.fixable else Text("")
                line = Text.assemble(
                    "  ", loc, " ", tag, " ", rule, fixable, "  ", f.message
                )
                self.console.print(line)
                self.console.print(Text(f"    > …{f.snippet}…", style="dim"))

        self.console.print()
        self._summary(findings, fixes_applied)

    def _summary(self, findings: list[Finding], fixes_applied: int) -> None:
        counts = Counter(f.severity for f in findings)
        table = Table(show_header=False, box=None, pad_edge=False)
        table.add_column(justify="right")
        table.add_column()
        table.add_row(
            Text(str(counts.get("error", 0)), style=_SEVERITY_STYLE["error"]),
            "errors",
        )
        table.add_row(
            Text(str(counts.get("warning", 0)), style=_SEVERITY_STYLE["warning"]),
            "warnings",
        )
        table.add_row(
            Text(str(counts.get("info", 0)), style=_SEVERITY_STYLE["info"]),
            "info",
        )
        if fixes_applied:
            table.add_row(Text(str(fixes_applied), style="green"), "fixes applied")
        self.console.print(table)
