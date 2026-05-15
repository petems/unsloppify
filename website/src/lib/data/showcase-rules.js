// Curated subset of rules from src/unsloppify/rules/*.yaml, chosen to show the
// flavour of each tier on the landing page. Not exhaustive -- see the repo for
// the full catalogue.

export const tiers = [
	{
		key: 'punctuation',
		name: 'Punctuation',
		blurb: 'Typography giveaways. Always safe to auto-fix.',
		fixable: 'auto',
		rules: [
			{ trigger: '--', note: 'em dash -> double hyphen' },
			{ trigger: '" "', note: 'smart quotes -> straight' },
			{ trigger: '...', note: 'ellipsis char -> three dots' },
			{ trigger: '\\u200B', note: 'zero-width space -> stripped' }
		]
	},
	{
		key: 'phrases',
		name: 'Banned phrases',
		blurb: 'Throat-clearing, business jargon, hype cliches. Curated swaps are auto-fixed; the rest are flagged.',
		fixable: 'mixed',
		rules: [
			{ trigger: 'delve into', note: 'cliche AI verb' },
			{ trigger: 'In today’s fast-paced world', note: 'error: cut the entire phrase' },
			{ trigger: 'Let that sink in', note: 'error: emphasis crutch' },
			{ trigger: 'Here’s the thing', note: 'throat-clearing' },
			{ trigger: 'deep dive', note: '-> examination (fixable)' },
			{ trigger: 'lean into', note: '-> embrace (fixable)' },
			{ trigger: 'circle back', note: '-> revisit (fixable)' },
			{ trigger: 'tapestry', note: 'almost never the right word' }
		]
	},
	{
		key: 'vocabulary',
		name: 'AI vocabulary',
		blurb: 'Single words flagged across multiple AI-detection studies. Replacement is judgment-dependent.',
		fixable: 'flag',
		rules: [
			{ trigger: 'delve', note: 'the single most-flagged AI marker' },
			{ trigger: 'seamless', note: 'show the seams aren’t there' },
			{ trigger: 'vibrant', note: 'pick a more specific word' },
			{ trigger: 'pivotal', note: 'key, important, or be specific' },
			{ trigger: 'meticulous', note: 'careful or thorough' },
			{ trigger: 'leverage', note: 'use “use”' },
			{ trigger: 'foster', note: 'build, create, or encourage' },
			{ trigger: 'paramount', note: 'critical, or be specific' }
		]
	},
	{
		key: 'structures',
		name: 'Structures',
		blurb: 'Patterns no regex can fix. The Claude skill rewrites these with judgment.',
		fixable: 'skill',
		rules: [
			{ trigger: 'It’s not X, it’s Y', note: 'binary contrast' },
			{ trigger: 'Not just X, but Y', note: 'additive hedge' },
			{ trigger: 'The X doesn’t do Y, it does Z', note: 'false agency' },
			{ trigger: 'Short. Punchy. Sentences.', note: 'parataxis cliche' },
			{ trigger: 'Whether you’re a beginner or expert', note: 'audience-pandering opener' }
		]
	}
];
