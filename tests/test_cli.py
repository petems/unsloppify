"""CLI tests via Typer's test runner."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from unsloppify.cli import app

runner = CliRunner()


@pytest.fixture
def slop_file(tmp_path: Path) -> Path:
    p = tmp_path / "slop.md"
    p.write_text(
        "# Title\n\nIn today's fast-paced world, we delve into things — daily.\n",
        encoding="utf-8",
    )
    return p


def test_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "unsloppify" in result.stdout


def test_list_rules():
    result = runner.invoke(app, ["--list-rules"])
    assert result.exit_code == 0
    assert "punct.em-dash" in result.stdout
    assert "vocab.delve" in result.stdout


def test_no_args_help():
    result = runner.invoke(app, [])
    # Typer's no_args_is_help — exits 0 or 2 depending on version
    assert "PATH" in result.stdout or "Usage" in result.stdout


def test_clean_file_exits_zero(tmp_path: Path):
    p = tmp_path / "clean.md"
    p.write_text("# Title\n\nClean prose with nothing flagged.\n", encoding="utf-8")
    result = runner.invoke(app, [str(p)])
    assert result.exit_code == 0


def test_dirty_file_exits_one(slop_file: Path):
    result = runner.invoke(app, [str(slop_file)])
    assert result.exit_code == 1


def test_fix_flag_rewrites_file(slop_file: Path):
    original = slop_file.read_text()
    result = runner.invoke(app, ["--fix", str(slop_file)])
    # exit code is 1 because non-fixable findings remain (delve, in-todays)
    assert result.exit_code in (0, 1)
    new_text = slop_file.read_text()
    assert "—" not in new_text  # em dash fixed
    assert new_text != original


def test_json_format(slop_file: Path):
    result = runner.invoke(app, ["--format", "json", str(slop_file)])
    assert result.exit_code == 1
    import json
    payload = json.loads(result.stdout)
    assert payload["version"] == 1
    assert payload["summary"]["total"] > 0
    assert "findings" in payload


def test_github_format(slop_file: Path):
    result = runner.invoke(app, ["--format", "github", str(slop_file)])
    assert result.exit_code == 1
    assert "::error" in result.stdout or "::warning" in result.stdout
    assert "title=unsloppify" in result.stdout


def test_severity_error_filters_out_lower(tmp_path: Path):
    p = tmp_path / "low.md"
    # only a 3-item list (severity info) — should pass --severity error
    p.write_text("apples, oranges, and bananas\n", encoding="utf-8")
    result = runner.invoke(app, ["--severity", "error", str(p)])
    assert result.exit_code == 0


def test_directory_recursion(tmp_path: Path):
    (tmp_path / "a.md").write_text("delve.\n", encoding="utf-8")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "b.md").write_text("tapestry.\n", encoding="utf-8")
    (tmp_path / "ignore.txt").write_text("delve\n", encoding="utf-8")
    result = runner.invoke(app, [str(tmp_path)])
    assert result.exit_code == 1
    assert "delve" in result.stdout
    assert "tapestry" in result.stdout
    assert "ignore.txt" not in result.stdout


def test_stdin_mode():
    result = runner.invoke(app, ["--stdin"], input="We delve into things.\n")
    assert result.exit_code == 1
    assert "delve" in result.stdout


def test_stdin_fix():
    result = runner.invoke(
        app,
        ["--stdin", "--fix"],
        input="He said — yes — to it.\n",
    )
    # stdout is the rewritten text
    assert "—" not in result.stdout
