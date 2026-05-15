"""Typer CLI entry point: `unsloppify`."""

from __future__ import annotations

import sys
from enum import StrEnum
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console

from unsloppify import __version__
from unsloppify.engine import (
    Finding,
    Rule,
    iter_markdown_files,
    load_rules,
    scan_file,
    scan_text,
)
from unsloppify.fixers import apply_fixes
from unsloppify.reporters import REPORTERS

app = typer.Typer(
    name="unsloppify",
    help="Strip AI slop from prose. Lints markdown for AI tells like em dashes, "
    "banned phrases, and structural cliches.",
    add_completion=False,
    no_args_is_help=True,
)
console = Console()


class Format(StrEnum):
    text = "text"
    json = "json"
    github = "github"


class Severity(StrEnum):
    info = "info"
    warning = "warning"
    error = "error"


_SEVERITY_RANK = {"info": 0, "warning": 1, "error": 2}


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"unsloppify {__version__}")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    paths: Annotated[
        list[Path] | None,
        typer.Argument(
            metavar="PATH",
            help="Files or directories to scan (recursive for dirs, .md/.mdx).",
        ),
    ] = None,
    fix: Annotated[
        bool,
        typer.Option("--fix", help="Rewrite files in place applying safe deterministic fixes."),
    ] = False,
    format_: Annotated[
        Format,
        typer.Option("--format", "-f", help="Output format."),
    ] = Format.text,
    severity: Annotated[
        Severity,
        typer.Option("--severity", "-s", help="Minimum severity to report."),
    ] = Severity.info,
    rules_path: Annotated[
        list[Path] | None,
        typer.Option(
            "--rules",
            "-r",
            help="Additional YAML rules file. Repeatable.",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ] = None,
    list_rules: Annotated[
        bool,
        typer.Option("--list-rules", help="Print all bundled rules and exit."),
    ] = False,
    stdin: Annotated[
        bool,
        typer.Option("--stdin", help="Read markdown from stdin instead of files."),
    ] = False,
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=_version_callback,
            is_eager=True,
            help="Show version and exit.",
        ),
    ] = False,
) -> None:
    """Scan markdown for AI writing patterns."""
    if ctx.invoked_subcommand is not None:
        return

    rules = load_rules(extra_paths=rules_path)

    if list_rules:
        _print_rules(rules)
        raise typer.Exit(code=0)

    if stdin:
        _run_stdin(rules, format_, severity, fix)
        return

    if not paths:
        console.print("[red]error:[/red] provide at least one PATH, or use --stdin.")
        raise typer.Exit(code=2)

    _run_paths(paths, rules, format_, severity, fix)


def _print_rules(rules: list[Rule]) -> None:
    by_cat: dict[str, list[Rule]] = {}
    for r in rules:
        by_cat.setdefault(r.category, []).append(r)
    for cat in sorted(by_cat):
        console.print(f"\n[bold]{cat}[/bold]")
        for r in sorted(by_cat[cat], key=lambda x: x.id):
            tag = "[fixable]" if r.fixable else ""
            console.print(f"  [dim]{r.severity:7}[/dim] {r.id} {tag}")
            console.print(f"    [dim]{r.message}[/dim]")


def _filter_severity(findings: list[Finding], min_sev: Severity) -> list[Finding]:
    threshold = _SEVERITY_RANK[min_sev.value]
    return [f for f in findings if _SEVERITY_RANK.get(f.severity, 0) >= threshold]


def _run_stdin(rules: list[Rule], format_: Format, severity: Severity, fix: bool) -> None:
    text = sys.stdin.read()
    fixes_applied = 0
    if fix:
        result = apply_fixes(text, rules)
        text = result.new_text
        fixes_applied = result.changes
        sys.stdout.write(text)
    findings = _filter_severity(
        list(scan_text(text, rules, Path("<stdin>"))),
        severity,
    )
    if not fix:
        _emit(findings, format_, fixes_applied)
    _exit_code(findings)


def _run_paths(
    paths: list[Path],
    rules: list[Rule],
    format_: Format,
    severity: Severity,
    fix: bool,
) -> None:
    files: list[Path] = []
    for p in paths:
        files.extend(iter_markdown_files(p))
    if not files:
        console.print("[yellow]no markdown files found.[/yellow]")
        raise typer.Exit(code=0)

    all_findings: list[Finding] = []
    fixes_applied = 0

    for file in files:
        if fix:
            text = file.read_text(encoding="utf-8")
            result = apply_fixes(text, rules)
            if result.changes:
                file.write_text(result.new_text, encoding="utf-8")
                fixes_applied += result.changes
            findings = list(scan_text(result.new_text, rules, file))
        else:
            findings = scan_file(file, rules)
        all_findings.extend(findings)

    filtered = _filter_severity(all_findings, severity)
    _emit(filtered, format_, fixes_applied)
    _exit_code(filtered)


def _emit(findings: list[Finding], format_: Format, fixes_applied: int) -> None:
    reporter_cls = REPORTERS[format_.value]
    reporter_cls().report(findings, fixes_applied=fixes_applied)


def _exit_code(findings: list[Finding]) -> None:
    if findings:
        raise typer.Exit(code=1)
    raise typer.Exit(code=0)
