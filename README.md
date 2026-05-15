# unsloppify

Strip AI slop from your prose. A fast CLI prose linter for markdown, plus a Claude Code skill and output-style for the judgment calls a regex can't make.

```bash
uvx unsloppify draft.md            # report findings, exit 1 if any
uvx unsloppify draft.md --fix      # rewrite safe deterministic fixes in place
uvx unsloppify docs/ --format json # recursive scan, JSON output
```

## Why this exists

Existing Claude skills like [stop-slop](https://github.com/hardikpandya/stop-slop) and [anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) ask Claude to scan your prose for tells. That works, but it costs tokens and Claude can miss obvious cases.

`unsloppify` splits the work:

| Tier | Examples | Handled by |
|------|----------|------------|
| 1. Punctuation | em dashes, smart quotes, ellipsis chars | CLI, auto-fixed |
| 2. Banned phrases | `delve into`, `tapestry`, `In today's fast-paced world` | CLI, flagged or auto-fixed |
| 3. Structures | binary contrasts, false agency, parataxis | Skill (LLM judgment) |

Run the CLI first to nuke the obvious stuff. Let the skill handle the rest.

## Install

```bash
uvx unsloppify --help               # one-shot, no install
pipx install unsloppify             # persistent CLI
uv add --dev unsloppify             # as a dev dep in a uv project
```

## Usage

### CLI

```bash
unsloppify FILE [FILE...]           # lint one or more files / directories
  --fix                             # apply safe fixes in place
  --format {text,json,github}       # output format (default: text)
  --severity {error,warning,info}   # minimum severity to report
  --rules PATH                      # add custom rules YAML
  --list-rules                      # print bundled rule catalogue
```

Exit codes: `0` clean, `1` findings present, `2` invocation error.

### Pre-commit

```yaml
repos:
  - repo: https://github.com/petems/unsloppify
    rev: v0.1.0
    hooks:
      - id: unsloppify
```

### GitHub Actions

```yaml
- run: uvx unsloppify docs/ --format github
```

### Claude Code skill

Two ways to install:

**Plugin marketplace** (recommended for Claude Code):

```text
/plugin marketplace add petems/unsloppify
/plugin install unsloppify@unsloppify
```

**Skills CLI** (works with Claude Code, Codex, Cursor, and other agents):

```bash
npx skills add petems/unsloppify
```

Then ask the agent to "unsloppify this draft" and it will invoke the CLI first for the deterministic catches, then do a judgment pass on structures.

### Claude Code output style

`cp output-styles/unsloppified.md ~/.claude/output-styles/` then `/output-style unsloppified`. Claude's own responses will avoid em dashes, banned phrases, and structural cliches.

## Rule catalogue

```bash
unsloppify --list-rules
```

Or browse `src/unsloppify/rules/*.yaml` directly. Rules are versioned with the package.

## Credit

The vocabulary lists and structural patterns are adapted from MIT-licensed upstream skills. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## License

MIT
