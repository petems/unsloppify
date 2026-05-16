<script>
	import { tiers } from '$lib/data/showcase-rules.js';

	function badge(fixable) {
		if (fixable === 'auto') return { text: 'auto-fix', cls: 'auto' };
		if (fixable === 'mixed') return { text: 'flag + fix', cls: 'mixed' };
		if (fixable === 'flag') return { text: 'flag only', cls: 'flag' };
		return { text: 'skill rewrite', cls: 'skill' };
	}

	function glyph(fixable) {
		if (fixable === 'auto') return '⌐';
		if (fixable === 'mixed') return '∧';
		if (fixable === 'flag') return '○';
		return '¶';
	}
</script>

<section class="rules" id="rules">
	<div class="rules-inner">
		<div class="folio-bar">
			<span class="eyebrow">the catalogue &nbsp;·&nbsp; a sample</span>
			<span class="folio">p. 03</span>
		</div>

		<header class="rules-header">
			<h2>
				<span class="sigil">§ V.</span>
				A taste of the catalogue
			</h2>
			<p class="lead">
				A sample of the bundled rules. Run <code>unsloppify --list-rules</code>
				for the full set, or browse the YAML at
				<a href="https://github.com/petems/unsloppify/tree/master/src/unsloppify/rules" target="_blank" rel="noopener noreferrer">src/unsloppify/rules/</a>.
			</p>
		</header>

		<div class="tier-stack">
			{#each tiers as tier, ti}
				{@const b = badge(tier.fixable)}
				{@const g = glyph(tier.fixable)}
				<article class="tier" data-cls={b.cls}>
					<header class="tier-head">
						<div class="tier-num">{String(ti + 1).padStart(2, '0')}</div>
						<div class="tier-meta">
							<div class="tier-title">
								<span class="tier-glyph" aria-hidden="true">{g}</span>
								<h3>{tier.name}</h3>
								<span class="tier-badge {b.cls}">{b.text}</span>
							</div>
							<p class="tier-blurb">{tier.blurb}</p>
						</div>
					</header>

					<table class="rule-table">
						<tbody>
							{#each tier.rules as rule, ri}
								<tr>
									<td class="rule-idx">{String(ri + 1).padStart(2, '0')}</td>
									<td class="rule-trigger"><code>{rule.trigger}</code></td>
									<td class="rule-note">{rule.note}</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</article>
			{/each}
		</div>
	</div>
</section>

<style>
	.rules {
		background:
			linear-gradient(90deg, oklch(0.88 0.035 224 / 0.55) 1px, transparent 1px),
			var(--paper-2);
		background-size: 96px 100%, auto;
		background-position: calc(50% - 486px) 0, 0 0;
		border-top: 1px solid var(--paper-rule);
		border-bottom: 1px solid var(--paper-rule);
		padding: 72px 32px 88px;
		position: relative;
	}

	.rules-inner {
		max-width: var(--col-wide);
		margin: 0 auto;
	}

	.folio-bar {
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		padding-bottom: 14px;
		margin-bottom: 56px;
		border-bottom: 1px solid var(--paper-rule);
	}

	.rules-header {
		max-width: var(--col-wide);
		width: 100%;
		margin-bottom: 48px;
		padding: 26px 30px 28px;
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 70%, var(--sheet-warm) 100%),
			var(--sheet);
		border: 1px solid var(--sheet-border);
		border-left: 5px solid var(--mark);
		box-shadow: var(--sheet-shadow);
		position: relative;
	}

	.rules-header::before {
		content: '';
		position: absolute;
		inset: -1px auto -1px -1px;
		width: 5px;
		background: linear-gradient(var(--mark), var(--pencil));
	}

	.rules-header h2 {
		font-family: var(--serif);
		font-size: 2rem;
		font-weight: 900;
		letter-spacing: 0;
		color: var(--ink);
		margin-bottom: 12px;
		display: flex;
		align-items: baseline;
		gap: 14px;
		font-variation-settings: 'opsz' 72;
	}

	.rules-header .sigil {
		font-family: var(--serif);
		font-style: italic;
		font-weight: 400;
		color: var(--mark);
		font-size: 1.4rem;
	}

	.lead {
		font-family: var(--serif);
		color: var(--ink-soft);
		font-size: 1.1rem;
		line-height: 1.6;
		font-variation-settings: 'opsz' 22;
	}

	.lead code {
		font-size: 0.85em;
	}

	.tier-stack {
		display: flex;
		flex-direction: column;
		gap: 18px;
	}

	.tier {
		padding: 28px 30px 30px;
		border: 1px solid var(--sheet-border);
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 64%, var(--sheet-blue) 100%),
			var(--sheet);
		box-shadow: var(--sheet-shadow);
		position: relative;
	}

	.tier::before {
		content: '';
		position: absolute;
		inset: -1px auto -1px -1px;
		width: 5px;
		background: var(--mark);
	}

	.tier-head {
		display: grid;
		grid-template-columns: 80px minmax(0, 1fr);
		gap: 24px;
		align-items: baseline;
		margin-bottom: 22px;
	}

	.tier-num {
		font-family: var(--mono);
		font-size: 2.2rem;
		font-weight: 600;
		color: var(--mark);
		letter-spacing: 0;
		line-height: 1;
		font-variant-numeric: tabular-nums;
	}

	.tier-title {
		display: flex;
		align-items: baseline;
		gap: 14px;
		flex-wrap: wrap;
		margin-bottom: 6px;
	}

	.tier-glyph {
		font-family: var(--serif);
		font-style: italic;
		color: var(--mark);
		font-size: 1.4rem;
		font-weight: 700;
		line-height: 0;
	}

	.tier-title h3 {
		font-family: var(--serif);
		font-size: 1.6rem;
		font-weight: 900;
		font-style: italic;
		color: var(--ink);
		letter-spacing: 0;
		font-variation-settings: 'opsz' 60, 'SOFT' 80;
	}

	.tier-badge {
		font-family: var(--mono);
		font-size: 0.66rem;
		font-weight: 600;
		padding: 3px 9px;
		letter-spacing: 0.12em;
		text-transform: uppercase;
		border: 1px solid currentColor;
		line-height: 1.4;
	}

	.tier-badge.auto {
		color: oklch(0.42 0.12 145);
		background: oklch(0.92 0.06 145);
		border-color: oklch(0.78 0.10 145);
	}

	.tier-badge.mixed {
		color: oklch(0.40 0.13 70);
		background: oklch(0.93 0.07 88);
		border-color: oklch(0.78 0.10 80);
	}

	.tier-badge.flag {
		color: var(--mark-hot);
		background: var(--mark-soft);
		border-color: oklch(0.75 0.13 30);
	}

	.tier-badge.skill {
		color: var(--pencil);
		background: var(--pencil-soft);
		border-color: oklch(0.70 0.08 252);
	}

	.tier-blurb {
		font-family: var(--serif);
		font-size: 1rem;
		font-style: italic;
		color: var(--ink-soft);
		line-height: 1.55;
		max-width: 640px;
		font-variation-settings: 'opsz' 22;
	}

	.rule-table {
		width: 100%;
		border-collapse: collapse;
		margin-left: 104px;
		max-width: calc(100% - 104px);
		background: oklch(1 0 0 / 0.48);
	}

	.rule-table tr {
		border-top: 1px dashed var(--paper-rule);
	}

	.rule-table tr:first-child {
		border-top: 1px solid var(--paper-rule);
	}

	.rule-table td {
		padding: 11px 16px 11px 0;
		vertical-align: baseline;
	}

	.rule-idx {
		font-family: var(--mono);
		font-size: 0.78rem;
		color: var(--ink-faint);
		width: 36px;
		font-variant-numeric: tabular-nums;
		letter-spacing: 0;
	}

	.rule-trigger {
		width: 38%;
	}

	.rule-trigger code {
		font-family: var(--mono);
		font-size: 0.86rem;
		background: var(--paper);
		padding: 3px 9px;
		border: 1px solid var(--paper-rule);
		color: var(--ink);
		white-space: nowrap;
	}

	.rule-note {
		font-family: var(--serif);
		font-size: 0.98rem;
		font-style: italic;
		color: var(--ink-soft);
		line-height: 1.5;
		font-variation-settings: 'opsz' 20;
	}

	@media (max-width: 820px) {
		.rule-table {
			margin-left: 0;
			max-width: 100%;
		}

		.tier-head {
			grid-template-columns: 60px minmax(0, 1fr);
			gap: 16px;
		}

		.tier-num {
			font-size: 1.6rem;
		}

		.tier-title h3 {
			font-size: 1.3rem;
		}
	}

	@media (max-width: 560px) {
		.rules {
			padding: 56px 22px 64px;
		}

		.rules-header h2 {
			font-size: 1.5rem;
		}

		.rule-table td {
			display: block;
			padding: 4px 0;
		}

		.rule-idx {
			width: auto;
			font-size: 0.7rem;
			letter-spacing: 0.08em;
			text-transform: uppercase;
		}

		.rule-trigger {
			width: auto;
			padding-bottom: 4px;
		}

		.rule-trigger code {
			white-space: normal;
			word-break: break-word;
		}

		.rule-table tr {
			padding: 12px 0;
		}
	}
</style>
