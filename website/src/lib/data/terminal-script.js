// Lines for the animated Terminal component. Each entry: { text, cls } where
// `cls` controls colour and slot delay (see Terminal.svelte's delay map).
// The script demonstrates the lint -> --fix loop with a residual judgment-call
// finding handed off to the Claude Code skill.

export const lines = [
	{ text: '$ uvx unsloppify draft.md', cls: 'cmd' },
	{ text: '', cls: 'blank' },
	{ text: '  draft.md', cls: 'label' },
	{ text: '    3:15  error    punctuation: em dash', cls: 'err' },
	{ text: '    7:1   warning  phrase: "In today\'s fast-paced world"', cls: 'warn' },
	{ text: '    7:42  warning  vocabulary: "delve"', cls: 'warn' },
	{ text: '    12:8  warning  vocabulary: "seamless"', cls: 'warn' },
	{ text: '', cls: 'blank' },
	{ text: '  4 findings (1 error, 3 warnings)', cls: 'summary' },
	{ text: '', cls: 'blank' },
	{ text: '$ uvx unsloppify draft.md --fix', cls: 'cmd-go' },
	{ text: '', cls: 'blank' },
	{ text: '  draft.md  fixed', cls: 'ok' },
	{ text: '    em dash         -> --', cls: 'fix' },
	{ text: '    "In today\'s ..." -> deleted', cls: 'fix' },
	{ text: '', cls: 'blank' },
	{ text: '  2 findings remain (judgment required)', cls: 'cyan' },
	{ text: '    vocab: "delve", "seamless"', cls: 'dim' },
	{ text: '', cls: 'blank' },
	{ text: '  ----', cls: 'rule' },
	{ text: '', cls: 'blank' },
	{ text: '$ claude /unsloppify draft.md', cls: 'cmd-go' },
	{ text: '', cls: 'blank' },
	{ text: '  Reading flagged ranges...', cls: 'cyan' },
	{ text: '  Rewriting "delve into"   -> "examine"', cls: 'ok' },
	{ text: '  Rewriting "seamless UX"  -> "the UX hides every transition"', cls: 'ok' },
	{ text: '', cls: 'blank' },
	{ text: '  unsloppified.', cls: 'done' }
];
