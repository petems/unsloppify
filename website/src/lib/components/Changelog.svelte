<section class="changelog" id="changelog">
	<div class="changelog-inner">
		<div class="folio-bar">
			<span class="eyebrow">revisions &nbsp;·&nbsp; changelog</span>
			<span class="folio">p. 05</span>
		</div>

		<div class="revision-sheet">
			<h2>
				<span class="sigil">§ VII.</span>
				Revision history
			</h2>

			<div class="changelog-list">
				<div class="changelog-entry">
					<aside class="changelog-meta">
						<span class="changelog-version">v0.1.0</span>
						<span class="changelog-date">15 May 2026</span>
						<span class="changelog-tag">first edition</span>
					</aside>
					<ul class="changelog-items">
						<li>Three-tier rule engine: punctuation auto-fix, banned-phrase swaps, structural flags</li>
						<li>120+ rules covering em dashes, smart quotes, AI vocabulary, throat-clearing openers, business jargon, hype, and structural cliches</li>
						<li>Outputs: <code>text</code>, <code>json</code>, and <code>github</code> annotations for CI</li>
						<li>Claude Code skill <code>/unsloppify</code>, a two-phase workflow with a five-dimension scoring rubric (Clarity, Specificity, Agency, Rhythm, Honesty)</li>
						<li>Claude Code output-style <code>unsloppified</code>, which patches Claude's own responses so the slop never appears in the first place</li>
						<li>Plugin marketplace listing and <a href="https://agentskills.io" target="_blank" rel="noopener noreferrer">Agent Skills</a>-compatible skill bundle</li>
						<li>Bring-your-own rules via <code>--rules path/to/rules.yaml</code></li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</section>

<style>
	.changelog {
		max-width: var(--col-wide);
		margin: 0 auto;
		padding: 88px 32px 56px;
	}

	.folio-bar {
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		padding-bottom: 14px;
		margin-bottom: 44px;
		border-bottom: 1px solid var(--paper-rule);
	}

	.revision-sheet {
		position: relative;
		padding: 30px 32px 34px;
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 68%, var(--sheet-warm) 100%),
			var(--sheet);
		border: 1px solid var(--sheet-border);
		border-left: 5px solid var(--mark);
		box-shadow: var(--sheet-shadow);
	}

	.revision-sheet::before {
		content: '';
		position: absolute;
		inset: -1px auto -1px -1px;
		width: 5px;
		background: linear-gradient(var(--mark), var(--pencil));
	}

	h2 {
		font-family: var(--serif);
		font-size: 1.8rem;
		font-weight: 900;
		letter-spacing: 0;
		margin-bottom: 32px;
		display: flex;
		align-items: baseline;
		gap: 14px;
		color: var(--ink);
		font-variation-settings: 'opsz' 64;
	}

	h2 .sigil {
		font-family: var(--serif);
		font-style: italic;
		font-weight: 400;
		color: var(--mark);
		font-size: 1.3rem;
	}

	.changelog-list {
		display: flex;
		flex-direction: column;
	}

	.changelog-entry {
		display: grid;
		grid-template-columns: 200px minmax(0, 1fr);
		gap: 48px;
		padding: 24px 0 0;
		border-top: 2px solid var(--ink);
	}

	.changelog-meta {
		display: flex;
		flex-direction: column;
		gap: 6px;
		padding-top: 4px;
	}

	.changelog-version {
		font-family: var(--mono);
		font-size: 1.4rem;
		font-weight: 600;
		color: var(--ink);
		letter-spacing: 0;
	}

	.changelog-date {
		font-family: var(--serif);
		font-style: italic;
		font-size: 0.92rem;
		color: var(--ink-muted);
	}

	.changelog-tag {
		display: inline-block;
		width: fit-content;
		margin-top: 6px;
		font-family: var(--mono);
		font-size: 0.66rem;
		font-weight: 600;
		text-transform: uppercase;
		letter-spacing: 0.12em;
		color: var(--mark);
		padding: 3px 9px;
		border: 1px solid var(--mark);
	}

	.changelog-items {
		margin: 0;
		padding-left: 0;
		font-family: var(--serif);
		color: var(--ink-soft);
		font-size: 1rem;
		line-height: 1.65;
		list-style: none;
		font-variation-settings: 'opsz' 20;
	}

	.changelog-items li {
		padding: 8px 0 8px 26px;
		position: relative;
		border-top: 1px dashed var(--paper-rule);
	}

	.changelog-items li:first-child {
		border-top: 0;
		padding-top: 2px;
	}

	.changelog-items li::before {
		content: '∧';
		position: absolute;
		left: 0;
		top: 8px;
		font-family: var(--mono);
		font-size: 0.85em;
		color: var(--mark);
		font-weight: 700;
	}

	.changelog-items li:first-child::before {
		top: 2px;
	}

	.changelog-items code {
		font-size: 0.85em;
	}

	.changelog-items a {
		color: var(--ink);
	}

	@media (max-width: 720px) {
		.changelog {
			padding: 56px 22px 36px;
		}

		.revision-sheet {
			padding: 24px 18px 26px;
		}

		.changelog-entry {
			grid-template-columns: 1fr;
			gap: 14px;
		}

		.changelog-meta {
			flex-direction: row;
			align-items: baseline;
			gap: 16px;
		}
	}
</style>
