# AGENTS.md

Guidance for AI assistants (Claude Code, Cursor, Codex, Gemini CLI, etc.) working on the `unsloppify` repo itself.

## What this project is

A CLI prose linter that strips characteristic AI-generated writing patterns from markdown. Ships alongside a Claude Code skill and an output-style file that apply the same rules at the LLM layer.

Three enforcement tiers:

1. **Punctuation** (em dashes, smart quotes) — regex, auto-fixable
2. **Banned phrases** (`delve into`, `In today's fast-paced world`) — regex, auto-fixable with literal swaps
3. **Structures** (binary contrasts, false agency) — flagged only; LLM judgment required

## Layout

```
src/unsloppify/         # Python package
  cli.py                # Typer entry point
  engine.py             # rule loading + scanning
  fixers.py             # safe deterministic rewrites
  reporters/            # text, json, github output formats
  rules/*.yaml          # bundled rule catalogues
skills/unsloppify/      # Claude Code skill (SKILL.md + references/)
output-styles/          # Claude Code output style file
tests/                  # pytest suite
```

## Commands

```bash
uv sync                              # install deps
uv run pytest                        # run tests
uv run ruff check src tests          # lint
uv run mypy src                      # type-check
uv run unsloppify README.md          # dogfood: lint our own README
uv run unsloppify README.md --fix    # apply safe fixes
```

## Rules

Rules live in `src/unsloppify/rules/*.yaml`. Each rule has `id`, `severity` (`error|warning|info`), `category`, `pattern` (regex), `message`, `fixable` (bool), optional `replacement`, and `examples`. Adding a rule:

1. Append to the appropriate YAML file. Choose `fixable: true` only for unambiguous replacements (em dash → comma is safe; "delve into" → "examine" is judgment-call territory and should stay `fixable: false`).
2. Add a fixture pair under `tests/fixtures/` and a test case in `tests/test_engine.py`.
3. Mirror the rule into `skills/unsloppify/references/phrases.md` or `structures.md` so the LLM-side skill stays in sync.

## Code-fence awareness

The engine skips content inside fenced code blocks (` ``` ` and `~~~`). Em dashes in code stay; em dashes in prose go. See `engine.py:_iter_prose_segments`.

## Where rules came from

The vocabulary lists and structural patterns are adapted from `hardikpandya/stop-slop` and `jalaalrd/anti-ai-slop-writing` (both MIT). See `THIRD_PARTY_NOTICES.md`. When porting more upstream content, preserve attribution.

## Self-lint

The repo's own markdown (README, AGENTS.md, skill files) must pass `uv run unsloppify .`. The pre-commit hook enforces this.

## What NOT to do here

- Don't add auto-fixes for tier-3 (structural) rules — those need LLM judgment.
- Don't bypass code-fence skipping for "convenience" — code examples must remain inviolate.
- Don't hard-code rule strings in Python — they live in YAML.
