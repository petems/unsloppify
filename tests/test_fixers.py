"""Fixer tests: deterministic rewrites with code-fence preservation."""

from unsloppify.engine import load_rules
from unsloppify.fixers import apply_fixes


def test_em_dash_replaced_in_prose():
    text = "Hello — world."
    result = apply_fixes(text, load_rules())
    assert "—" not in result.new_text
    assert result.changes >= 1


def test_em_dash_preserved_in_code_fence():
    text = "Hello — world.\n\n```\n# em — in code\n```\n"
    result = apply_fixes(text, load_rules())
    # prose em dash is gone
    assert result.new_text.split("```")[0].count("—") == 0
    # code-fence em dash stays
    assert "—" in result.new_text.split("```")[1]


def test_em_dash_preserved_in_inline_code():
    text = "Use `a — b` here. But — not in prose."
    result = apply_fixes(text, load_rules())
    # inline-code em dash stays
    assert "`a — b`" in result.new_text
    # prose em dash gone
    assert result.new_text.count("—") == 1


def test_jargon_swap_lean_into():
    text = "We need to lean into the work."
    result = apply_fixes(text, load_rules())
    assert "lean into" not in result.new_text
    assert "embrace" in result.new_text


def test_utilize_swap():
    text = "We utilize this tool daily."
    result = apply_fixes(text, load_rules())
    assert "utilize" not in result.new_text.lower()
    assert "use" in result.new_text.lower()


def test_smart_quotes_replaced():
    text = "He said “hello” to her."
    result = apply_fixes(text, load_rules())
    assert "“" not in result.new_text
    assert "”" not in result.new_text
    assert '"hello"' in result.new_text


def test_zero_width_stripped():
    text = "Hello​world"
    result = apply_fixes(text, load_rules())
    assert "​" not in result.new_text
    assert "Helloworld" in result.new_text


def test_no_changes_returns_original():
    text = "Plain ascii prose with nothing wrong."
    result = apply_fixes(text, load_rules())
    assert result.new_text == text
    assert result.changes == 0


def test_frontmatter_protected():
    text = "---\ntitle: lean into things\n---\n\nWe lean into the work.\n"
    result = apply_fixes(text, load_rules())
    # frontmatter "lean into" survives
    assert "lean into" in result.new_text.split("---")[1]
    # prose "lean into" is replaced
    body = result.new_text.split("---\n", 2)[-1]
    assert "lean into" not in body
    assert "embrace" in body
