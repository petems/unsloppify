"""Engine tests: rule loading, prose segmentation, finding emission."""

from pathlib import Path

import pytest

from unsloppify.engine import (
    Finding,
    Rule,
    _mask_skipped_regions,
    load_rules,
    scan_text,
)


def test_load_rules_returns_rules():
    rules = load_rules()
    assert len(rules) > 50, "expected the bundled catalogue to be sizeable"
    assert all(isinstance(r, Rule) for r in rules)
    ids = {r.id for r in rules}
    assert "punct.em-dash" in ids
    assert "vocab.delve" in ids
    assert "phrases.in-todays" in ids


def test_load_rules_dedups_by_id(tmp_path):
    dup = tmp_path / "dup.yaml"
    dup.write_text(
        "category: x\nrules:\n"
        "  - id: punct.em-dash\n    pattern: '-'\n    message: dup\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Duplicate rule id"):
        load_rules(extra_paths=[dup])


def test_em_dash_flagged():
    text = "He was — and remained — uncertain."
    rules = load_rules()
    findings = list(scan_text(text, rules, Path("x.md")))
    em = [f for f in findings if f.rule_id == "punct.em-dash"]
    assert len(em) == 2


def test_code_fence_is_skipped():
    text = (
        "Real prose with delve.\n\n"
        "```python\n"
        "# also delve, but inside code\n"
        "x = 'delve'\n"
        "```\n\n"
        "More prose with tapestry.\n"
    )
    rules = load_rules()
    findings = list(scan_text(text, rules, Path("x.md")))
    # delve should fire once (prose), not in code
    delve = [f for f in findings if f.rule_id == "vocab.delve"]
    assert len(delve) == 1, [f.line for f in delve]
    assert delve[0].line == 1
    # tapestry fires once in the prose after the fence
    tapestry = [f for f in findings if f.rule_id == "vocab.tapestry"]
    assert len(tapestry) == 1
    assert tapestry[0].line == 8


def test_inline_code_is_skipped():
    text = "Use the `delve` function. But don't delve into the data."
    rules = load_rules()
    findings = [f for f in scan_text(text, rules, Path("x.md")) if f.rule_id == "vocab.delve"]
    # only the prose "delve", not the inline-code one
    assert len(findings) == 1
    assert findings[0].column > 30  # past the inline code span


def test_frontmatter_is_skipped():
    text = (
        "---\n"
        "title: delve into things\n"
        "tags: [tapestry]\n"
        "---\n\n"
        "Real prose with delve.\n"
    )
    rules = load_rules()
    findings = [f for f in scan_text(text, rules, Path("x.md")) if f.rule_id == "vocab.delve"]
    assert len(findings) == 1
    assert findings[0].line == 6


def test_opener_does_not_match_after_blank_lines():
    """Regression: Moreover/Furthermore opener regex used to greedy-match newlines."""
    text = (
        "Some prose.\n\n"
        "```\nclean code\n```\n\n"
        "Furthermore, the second paragraph.\n"
    )
    rules = load_rules()
    findings = [
        f for f in scan_text(text, rules, Path("x.md")) if f.rule_id == "openers.furthermore"
    ]
    assert len(findings) == 1
    assert findings[0].line == 7


def test_line_and_column_are_one_indexed():
    text = "ab\ncde —fgh"
    rules = load_rules()
    em = [f for f in scan_text(text, rules, Path("x.md")) if f.rule_id == "punct.em-dash"]
    assert len(em) == 1
    assert em[0].line == 2
    assert em[0].column == 5  # after "cde "


def test_severity_filtering_via_rank():
    rules = load_rules()
    # delve is error
    text = "We delve into things."
    findings = list(scan_text(text, rules, Path("x.md")))
    assert any(f.severity == "error" for f in findings)


def test_mask_preserves_offsets_and_newlines():
    text = "abc\n```\ndef\n```\nxyz\n"
    masked = _mask_skipped_regions(text)
    assert len(masked) == len(text)
    assert masked.count("\n") == text.count("\n")
    # the fence interior must be neutralized
    assert "def" not in masked


def test_finding_dataclass_fields():
    text = "We delve."
    rules = load_rules()
    f = next(iter(scan_text(text, rules, Path("a.md"))))
    assert isinstance(f, Finding)
    assert f.fixable in (True, False)
    assert f.message
    assert f.snippet
