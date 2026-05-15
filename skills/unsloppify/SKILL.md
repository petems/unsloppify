---
name: unsloppify
description: Strip AI writing patterns from prose. Run the unsloppify CLI to auto-fix the deterministic stuff (em dashes, banned phrases, smart quotes), then rewrite structural cliches by hand. Use when drafting, editing, or reviewing markdown that needs to not read as AI-generated.
metadata:
  trigger: Editing markdown, blog drafts, READMEs, or any prose where the user says "unsloppify", "remove AI tells", "anti-slop", "stop slop", or "make this sound human"
---

# unsloppify

Strip characteristic AI writing patterns from prose. This skill pairs with the `unsloppify` Python CLI, which lives at https://github.com/petems/unsloppify and is installable via `uvx unsloppify`.

## Workflow

When asked to unsloppify a piece of prose:

1. **Hard-lock pass with the CLI.** Run `uvx unsloppify <file> --fix` on the target file. This auto-rewrites unambiguous catches: em dashes become commas, "lean into" becomes "embrace", smart quotes become straight quotes, and so on. Show the user the diff.
2. **Re-scan for findings the CLI can detect but not fix.** Run `uvx unsloppify <file>` (no `--fix`). The remaining findings are judgment calls: banned vocabulary (`delve`, `tapestry`), sentence openers (`Moreover,`, `Furthermore,`), structural cliches (binary contrasts, false agency).
3. **Judgment pass: rewrite each remaining finding.** For each one, decide whether to delete, rephrase, or leave (some are genuinely the right word in context). Apply the rules in `references/` to guide rewrites. Don't ask permission for each one — make the call and show the user the result.
4. **Self-check with the rubric.** Score the rewritten prose using `references/rubric.md`. If it scores below 35/50, revise again.
5. **Verify clean.** Final pass: `uvx unsloppify <file>` should exit 0 (or only have rule IDs you've consciously chosen to keep).

## CLI quick reference

```bash
uvx unsloppify path.md                   # lint, exit 1 on findings
uvx unsloppify path.md --fix             # rewrite safe deterministic fixes
uvx unsloppify path.md --format json     # machine-readable
uvx unsloppify --list-rules              # show all bundled rules
uvx unsloppify path.md --severity error  # only errors
```

If `uvx` isn't available, fall back to `pipx install unsloppify` then `unsloppify`.

## What gets auto-fixed (tier 1 + 2)

These are handled by the CLI's `--fix` mode — you don't have to think about them:

- Punctuation: em dashes (—), en dashes in prose, smart quotes, ellipsis chars, non-breaking spaces, zero-width characters, double exclamation marks
- Business jargon swaps: `lean into` → `embrace`, `circle back` → `revisit`, `deep dive` → `examination`, `moving forward` → `next`, `utilize` → `use`

## What you have to judgment-call (tier 3)

These the CLI flags but won't fix — that's your job:

- **Banned vocabulary** (`delve`, `tapestry`, `pivotal`, `vibrant`, `bolster`, `garner`, `underscore`, `multifaceted`, `foster`, `leverage`, `paramount`, `groundbreaking`, `cutting-edge`, `transformative`, `seamless`, `aforementioned`, `harness`, `spearhead`, `unprecedented`, `profound`, `empower`). See [references/phrases.md](references/phrases.md).
- **Sentence openers** (`Moreover,`, `Furthermore,`, `Additionally,`, `Interestingly,`, `Notably,`, `Importantly,`, `Indeed,`, `Overall,`, `Certainly,`, `Absolutely,`, `Great question!`, `As an AI`, `As a language model`, `I'd be happy to`).
- **Throat-clearing openers** (`Here's the thing`, `Let me be clear`, `The truth is`, `It turns out`, `The uncomfortable truth is`).
- **Structural cliches** — see [references/structures.md](references/structures.md):
  - Binary contrasts ("Not X, but Y" / "Not because X, but because Y" / "The problem isn't X, it's Y")
  - Negative listing ("Not a X. Not a Y. A Z.")
  - Dramatic fragmentation ("That's it. That's the thing.")
  - Rhetorical setups ("What if X?", "Here's what I mean:", "Think about it:")
  - False agency ("the culture shifts", "the decision emerges", "the data tells us")
  - Narrator-from-a-distance ("Nobody designed this", "This happens because")
  - Passive voice that hides actors
  - Three-item lists used reflexively
- **Lazy extremes** (`always`, `never`, `everyone`, `nobody`) doing vague work.
- **Empty adverbs** (`really`, `just`, `literally`, `genuinely`, `actually`).

## Rewrite principles

Adapted from the upstream skills this is built on. The full source is in `references/`.

1. **Cut throat-clearing.** State the point. Don't announce it.
2. **Active voice.** Every sentence needs a human subject doing something. Name the actor.
3. **Be specific.** No vague declaratives. Name the thing.
4. **Put the reader in the room.** "You" beats "people". Concrete beats abstract.
5. **Vary rhythm.** Mix sentence lengths. Two items beat three. Connect short sentences with conjunctions, semicolons, or commas to break parataxis.
6. **Trust readers.** Skip the softening, the justification, the hand-holding.
7. **Cut quotables.** If it sounds like a pull-quote, rewrite it.
8. **Show, don't describe.** "Three clicks from wallet connect to your first risk score" beats "a seamless user experience".
9. **Include friction.** Real human writing has doubt, mess, specific dates and times.

## Apply silently

Don't say "as per the unsloppify rules" or "applying rule X". Just rewrite. The user can see the diff.

## References

- [references/phrases.md](references/phrases.md) — banned phrases and vocabulary
- [references/structures.md](references/structures.md) — structural patterns
- [references/examples.md](references/examples.md) — before/after rewrites
- [references/rubric.md](references/rubric.md) — five-dimension scoring

## Credit

Vocabulary and structural rules adapted from MIT-licensed:
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) — the five-dimension rubric, structural patterns, business-jargon swaps
- [jalaalrd/anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) — banned vocabulary list, parataxis rules, accuracy rules

## License

MIT
