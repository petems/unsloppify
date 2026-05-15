"""Validate skill + plugin metadata files.

These tests guard the install-experience contracts:
- SKILL.md frontmatter must parse and stay within the Anthropic-allowed key set
  (otherwise the Claude app refuses to load the skill).
- .claude-plugin/marketplace.json + plugin.json must satisfy the Claude Code
  plugin marketplace schema enough to load via `/plugin marketplace add` and
  `/plugin install`.
- plugin.json version must stay in sync with pyproject.toml.
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any, cast

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = REPO_ROOT / "skills" / "unsloppify" / "SKILL.md"
MARKETPLACE_JSON = REPO_ROOT / ".claude-plugin" / "marketplace.json"
PLUGIN_JSON = REPO_ROOT / ".claude-plugin" / "plugin.json"
PYPROJECT_TOML = REPO_ROOT / "pyproject.toml"

ALLOWED_SKILL_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
}

KEBAB_CASE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_LIKE = re.compile(r"^\d+\.\d+\.\d+(?:[-+].+)?$")


def _parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise AssertionError(f"{path} does not start with YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise AssertionError(f"{path} frontmatter is not closed by a second '---'")
    parsed = yaml.safe_load(parts[1])
    assert isinstance(parsed, dict), f"{path} frontmatter is not a mapping"
    return cast(dict[str, Any], parsed)


@pytest.fixture(scope="module")
def skill_frontmatter() -> dict[str, Any]:
    return _parse_frontmatter(SKILL_MD)


@pytest.fixture(scope="module")
def marketplace() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(MARKETPLACE_JSON.read_text(encoding="utf-8")))


@pytest.fixture(scope="module")
def plugin() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(PLUGIN_JSON.read_text(encoding="utf-8")))


def test_skill_md_required_fields(skill_frontmatter: dict[str, Any]) -> None:
    assert "name" in skill_frontmatter, "SKILL.md must declare a name"
    assert "description" in skill_frontmatter, "SKILL.md must declare a description"
    name = skill_frontmatter["name"]
    assert isinstance(name, str) and KEBAB_CASE.match(name), (
        f"name must be kebab-case, got {name!r}"
    )
    description = skill_frontmatter["description"]
    assert isinstance(description, str) and description.strip(), (
        "description must be a non-empty string"
    )


def test_skill_md_only_allowed_keys(skill_frontmatter: dict[str, Any]) -> None:
    extra = set(skill_frontmatter.keys()) - ALLOWED_SKILL_FRONTMATTER_KEYS
    assert not extra, (
        f"SKILL.md has frontmatter keys outside the Anthropic-allowed set "
        f"{sorted(ALLOWED_SKILL_FRONTMATTER_KEYS)}: {sorted(extra)}. "
        "The Claude app rejects skills with unexpected top-level keys "
        "(use metadata: for free-form extras)."
    )


def test_marketplace_json_required_fields(marketplace: dict[str, Any]) -> None:
    assert marketplace.get("name"), "marketplace.json must declare a name"
    owner = marketplace.get("owner")
    assert isinstance(owner, dict) and owner.get("name"), (
        "marketplace.json must declare owner.name"
    )
    plugins = marketplace.get("plugins")
    assert isinstance(plugins, list) and plugins, (
        "marketplace.json must list at least one plugin"
    )
    for entry in plugins:
        assert isinstance(entry, dict)
        assert entry.get("name"), "every plugin entry needs a name"
        assert "source" in entry, "every plugin entry needs a source"
        if isinstance(entry["source"], str):
            assert entry["source"].startswith("./"), (
                f"local plugin source must start with './' (got {entry['source']!r})"
            )


def test_plugin_json_required_fields(plugin: dict[str, Any]) -> None:
    assert plugin.get("name"), "plugin.json must declare a name"
    assert plugin.get("description"), "plugin.json must declare a description"
    version = plugin.get("version")
    assert isinstance(version, str) and SEMVER_LIKE.match(version), (
        f"plugin.json version must be semver-like, got {version!r}"
    )


def test_marketplace_plugin_matches_plugin_manifest(
    marketplace: dict[str, Any],
    plugin: dict[str, Any],
) -> None:
    names = [p.get("name") for p in marketplace["plugins"]]
    assert plugin["name"] in names, (
        f"plugin.json name {plugin['name']!r} not listed in marketplace.json plugins"
    )


def test_plugin_version_matches_pyproject(plugin: dict[str, Any]) -> None:
    pyproject = tomllib.loads(PYPROJECT_TOML.read_text(encoding="utf-8"))
    py_version = pyproject["project"]["version"]
    assert plugin["version"] == py_version, (
        f"plugin.json version ({plugin['version']!r}) must match "
        f"pyproject.toml version ({py_version!r}). Bump both together."
    )


def test_skill_directory_matches_plugin_skill_name(
    skill_frontmatter: dict[str, Any],
) -> None:
    # The skill directory name should match the SKILL.md `name` so Claude Code's
    # auto-discovery (which looks at <skill-dir>/SKILL.md) doesn't surface
    # mismatched identifiers.
    assert SKILL_MD.parent.name == skill_frontmatter["name"], (
        f"skill directory {SKILL_MD.parent.name!r} must match SKILL.md name "
        f"{skill_frontmatter['name']!r}"
    )


def test_python_version_is_modern_enough() -> None:
    # tomllib requires 3.11+; pyproject pins >=3.11 already. Belt + braces.
    assert sys.version_info >= (3, 11), "tests require Python 3.11+ for tomllib"
