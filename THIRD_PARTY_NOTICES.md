# Third-Party Notices

`unsloppify` borrows rule content and skill design ideas from the following MIT-licensed projects. The CLI implementation is original; the rule catalogues, banned-phrase lists, and structural patterns are derived from these upstream sources and remain under their original licenses.

## stop-slop

- Repository: https://github.com/hardikpandya/stop-slop
- Author: Hardik Pandya (https://hvpandya.com)
- License: MIT

Source of the throat-clearing openers, emphasis crutches, business jargon table, adverb hitlist, vague declaratives, binary-contrast patterns, false-agency patterns, narrator-from-a-distance examples, the five-dimension scoring rubric (directness, rhythm, trust, authenticity, density), and several before/after examples.

## anti-ai-slop-writing

- Repository: https://github.com/jalaalrd/anti-ai-slop-writing
- License: MIT

Source of the banned-vocabulary list (50+ flagged words including "delve", "tapestry", "pivotal"), the era-specific AI vocabulary buckets, model-specific first-word tells (ChatGPT/Claude/Grok/Gemini/DeepSeek), formatting rules (markdown-in-DM tells, emoji-bullet patterns), and the structural rules around parataxis, hedging-seesaw, and uniform sentence length.

## MIT License (applies to both upstream projects)

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

## Additional References (not vendored)

- Wikipedia: ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — curated public list of AI tells, used as a sanity check on the rule set.
- [Vale](https://vale.sh/) — prose linter. Inspired the severity-level taxonomy. No code reuse.
