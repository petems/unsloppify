<section class="pitch">
	<div class="folio-bar">
		<span class="eyebrow">the split &nbsp;·&nbsp; how it works</span>
		<span class="folio">p. 02</span>
	</div>

	<article class="row">
		<header class="row-head">
			<span class="sigil">§ I.</span>
			<h2>The specimen</h2>
		</header>
		<div class="row-body">
			<p class="lead">
				Other anti-slop skills hand a draft to Claude and ask it to look for
				the tells. That works, but it costs tokens and the obvious cases slip
				past. <code>unsloppify</code> splits the work three ways.
			</p>

			<!-- Live galley specimen. The same paragraph as it lands in the linter, and the same paragraph after the proofreader is done. -->
			<figure class="galley">
				<figcaption class="galley-cap">
					<span class="galley-tag">before</span>
					<span class="galley-meta">draft.md &nbsp;·&nbsp; 4 findings</span>
				</figcaption>
				<p class="galley-prose">
					<span class="dele">In today&rsquo;s fast-paced world,</span>
					we wanted to <span class="dele">delve into</span>
					<span class="ins">examine</span>
					the <span class="dele">vibrant tapestry</span>
					<span class="ins">range</span> of
					<span class="dele">seamless</span>
					<span class="ins">unbroken</span> integrations.
					<span class="dele">Let that sink in.</span>
					<span class="margin-note" aria-hidden="true">
						<span class="mn-mark">⌐</span>
						<span class="mn-text">remove 'throat-clearing' AI phrases</span>
					</span>
				</p>
				<figcaption class="galley-cap galley-cap--after">
					<span class="galley-tag galley-tag--clean">after</span>
					<span class="galley-meta">unsloppified.md &nbsp;·&nbsp; clean</span>
				</figcaption>
				<p class="galley-prose galley-prose--clean">
					We wanted to examine the range of unbroken integrations.
				</p>
			</figure>
		</div>
	</article>

	<svg class="pencil-divider" viewBox="0 0 800 8" preserveAspectRatio="none" aria-hidden="true">
		<path d="M 0 4 Q 100 1, 200 4 T 400 4 T 600 5 T 800 3" stroke="currentColor" stroke-width="1.2" fill="none" />
	</svg>

	<article class="row">
		<header class="row-head">
			<span class="sigil">§ II.</span>
			<h2>The apparatus</h2>
		</header>
		<div class="row-body">
			<ol class="apparatus">
				<li>
					<span class="ap-num">01</span>
					<div class="ap-body">
						<h3>CLI</h3>
						<p>
							Three-tier rule engine. Auto-fixes em dashes, smart quotes,
							and a curated set of jargon swaps. Exits with code <code>1</code>
							on findings, so it drops into any CI or pre-commit pipeline
							without ceremony.
						</p>
					</div>
					<span class="ap-glyph" aria-hidden="true">∧</span>
				</li>
				<li>
					<span class="ap-num">02</span>
					<div class="ap-body">
						<h3>Skill</h3>
						<p>
							A two-phase Claude Code workflow: the CLI removes the obvious
							punctuation tells first, then a judgment pass handles
							vocabulary, openers, and structures. Scored against a
							five-dimension rubric.
						</p>
					</div>
					<span class="ap-glyph" aria-hidden="true">¶</span>
				</li>
				<li>
					<span class="ap-num">03</span>
					<div class="ap-body">
						<h3>Output style</h3>
						<p>
							A Claude Code output-style that patches Claude&rsquo;s own
							voice so the slop never appears in the first place. The
							preventative half of the prescription.
						</p>
					</div>
					<span class="ap-glyph" aria-hidden="true">⌐</span>
				</li>
			</ol>
		</div>
	</article>

	<svg class="pencil-divider" viewBox="0 0 800 8" preserveAspectRatio="none" aria-hidden="true">
		<path d="M 0 4 Q 120 6, 240 3 T 480 5 T 720 2 T 800 4" stroke="currentColor" stroke-width="1.2" fill="none" />
	</svg>

	<article class="row">
		<header class="row-head">
			<span class="sigil">§ III.</span>
			<h2>Three tiers of correction</h2>
		</header>
		<div class="row-body">
			<p>
				Every rule lives in one of three tiers. The tier decides whether a
				regex can fix it, flag it, or whether the call belongs to a human or
				an LLM with judgment.
			</p>
			<dl class="tiers">
				<div class="tier">
					<dt>
						<span class="tier-glyph" aria-hidden="true">⌐</span>
						Punctuation
					</dt>
					<dd>Em dashes, smart quotes, ellipsis chars, zero-width chars. <strong>Auto-fixed.</strong></dd>
				</div>
				<div class="tier">
					<dt>
						<span class="tier-glyph" aria-hidden="true">∧</span>
						Banned phrases
					</dt>
					<dd>Throat-clearing, business jargon, hype cliches. <strong>Flagged; a curated subset is auto-fixed.</strong></dd>
				</div>
				<div class="tier">
					<dt>
						<span class="tier-glyph" aria-hidden="true">¶</span>
						Structures
					</dt>
					<dd>Binary contrasts, false agency, parataxis. <strong>Flagged for the skill to rewrite.</strong></dd>
				</div>
			</dl>
		</div>
	</article>

	<svg class="pencil-divider" viewBox="0 0 800 8" preserveAspectRatio="none" aria-hidden="true">
		<path d="M 0 5 Q 80 3, 160 4 T 320 5 T 560 3 T 800 4" stroke="currentColor" stroke-width="1.2" fill="none" />
	</svg>

	<article class="row row--compact">
		<header class="row-head">
			<span class="sigil">§ IV.</span>
			<h2>Works with</h2>
		</header>
		<div class="row-body">
			<p>
				<strong>CLI</strong>: uvx, pipx, pre-commit, GitHub Actions, any
				language-agnostic CI runner.
			</p>
			<p>
				<strong>Agents</strong>: Claude Code (plugin marketplace + Agent
				Skills) and any other agent supporting
				<a href="https://agentskills.io" target="_blank" rel="noopener noreferrer">Agent Skills</a>.
			</p>
		</div>
	</article>
</section>

<style>
	.pitch {
		max-width: var(--col-wide);
		margin: 0 auto;
		padding: 42px 32px 64px;
		position: relative;
	}

	.folio-bar {
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		padding-bottom: 14px;
		margin-bottom: 64px;
		border-bottom: 1px solid var(--paper-rule);
	}

	.row {
		display: grid;
		grid-template-columns: 224px minmax(0, 1fr);
		gap: 48px;
		align-items: start;
		max-width: 980px;
		margin: 0 auto;
	}

	.row--compact .row-body p {
		margin-bottom: 6px;
	}

	.row--compact .row-body {
		padding: 22px 24px;
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 70%, var(--sheet-warm) 100%),
			var(--sheet);
		border: 1px solid var(--sheet-border);
		border-left: 5px solid var(--mark);
		box-shadow: var(--sheet-shadow);
		position: relative;
	}

	.row--compact .row-body::before {
		content: '';
		position: absolute;
		inset: -1px auto -1px -1px;
		width: 5px;
		background: linear-gradient(var(--mark), var(--pencil));
	}

	.row-head {
		display: flex;
		flex-direction: column;
		gap: 6px;
		padding-top: 6px;
	}

	.sigil {
		font-family: var(--serif);
		font-style: italic;
		font-size: 1.4rem;
		color: var(--mark);
		font-weight: 400;
		font-variation-settings: 'opsz' 144;
		line-height: 1;
	}

	.row-head h2 {
		font-family: var(--serif);
		font-size: 1.6rem;
		font-weight: 900;
		letter-spacing: 0;
		line-height: 1.05;
		color: var(--ink);
		font-variation-settings: 'opsz' 36, 'SOFT' 30;
	}

	.row-body {
		font-family: var(--serif);
		font-size: 1.04rem;
		line-height: 1.65;
		color: var(--ink-soft);
		font-variation-settings: 'opsz' 22;
	}

	.row-body p {
		margin-bottom: 14px;
	}

	.row-body p:last-child {
		margin-bottom: 0;
	}

	.row-body .lead {
		font-size: 1.12rem;
		color: var(--ink);
		font-weight: 500;
		margin-bottom: 22px;
		line-height: 1.55;
	}

	.row-body strong {
		color: var(--ink);
		font-weight: 700;
	}

	/* Galley specimen */
	.galley {
		margin: 28px 0 4px;
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 62%, var(--sheet-blue) 100%),
			var(--sheet);
		border: 1px solid var(--sheet-border);
		border-left: 8px solid var(--mark);
		padding: 24px 30px 26px;
		position: relative;
		box-shadow:
			10px 10px 0 oklch(0.90 0.035 224),
			var(--sheet-shadow);
	}

	.galley-cap {
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		margin-bottom: 12px;
		font-family: var(--mono);
		font-size: 0.72rem;
		letter-spacing: 0.04em;
	}

	.galley-cap--after {
		margin-top: 22px;
		padding-top: 14px;
		border-top: 1px dashed var(--paper-rule);
	}

	.galley-tag {
		font-weight: 700;
		text-transform: uppercase;
		color: var(--mark);
		padding: 2px 8px;
		background: var(--mark-soft);
		letter-spacing: 0.04em;
	}

	.galley-tag--clean {
		color: var(--pencil);
		background: var(--pencil-soft);
	}

	.galley-meta {
		color: var(--ink-faint);
	}

	.galley-prose {
		font-family: var(--serif);
		font-size: 1.06rem;
		line-height: 1.85;
		color: var(--ink);
		font-variation-settings: 'opsz' 22;
		position: relative;
		margin: 0;
	}

	.galley-prose--clean {
		color: var(--ink-soft);
		font-style: italic;
	}

	.dele {
		position: relative;
		color: var(--ink-faint);
		text-decoration: line-through;
		text-decoration-color: var(--mark);
		text-decoration-thickness: 2px;
		text-decoration-skip-ink: none;
	}

	.ins {
		display: inline-block;
		color: var(--pencil);
		font-style: italic;
		font-weight: 600;
		background: var(--pencil-soft);
		padding: 0 5px;
		margin: 0 2px;
		position: relative;
	}

	.ins::before {
		content: '∧';
		position: absolute;
		left: 50%;
		bottom: -8px;
		transform: translateX(-50%);
		font-family: var(--mono);
		font-size: 0.7em;
		color: var(--pencil);
		font-weight: 700;
	}

	.margin-note {
		position: absolute;
		right: -148px;
		top: 0;
		display: flex;
		align-items: baseline;
		gap: 8px;
		font-family: var(--serif);
		font-style: italic;
		font-size: 0.86rem;
		color: var(--mark);
		max-width: 130px;
		line-height: 1.4;
	}

	.mn-mark {
		font-size: 1.4rem;
		font-weight: 700;
		line-height: 0;
	}

	/* Apparatus list */
	.apparatus {
		list-style: none;
		padding: 0;
		margin: 8px 0 0;
	}

	.apparatus li {
		display: grid;
		grid-template-columns: 56px minmax(0, 1fr) 32px;
		gap: 18px;
		align-items: start;
		padding: 18px 18px;
		margin-bottom: 12px;
		border: 1px solid var(--sheet-border);
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 70%, var(--sheet-warm) 100%),
			var(--sheet);
		box-shadow: 0 10px 24px oklch(0.22 0.030 250 / 0.08);
	}

	.apparatus li:last-child {
		margin-bottom: 0;
	}

	.ap-num {
		font-family: var(--mono);
		font-size: 1.2rem;
		font-weight: 600;
		color: var(--mark);
		letter-spacing: 0;
		line-height: 1;
		padding-top: 6px;
	}

	.ap-body h3 {
		font-family: var(--serif);
		font-size: 1.18rem;
		font-weight: 700;
		font-style: italic;
		color: var(--ink);
		margin-bottom: 4px;
		font-variation-settings: 'opsz' 36, 'SOFT' 50;
	}

	.ap-body p {
		font-family: var(--serif);
		font-size: 1rem;
		line-height: 1.6;
		color: var(--ink-soft);
		margin: 0;
		font-variation-settings: 'opsz' 18;
	}

	.ap-glyph {
		font-family: var(--serif);
		font-style: italic;
		font-size: 1.6rem;
		color: var(--mark);
		opacity: 0.5;
		text-align: right;
		line-height: 1.2;
	}

	/* Tier list */
	.tiers {
		margin: 22px 0 0;
	}

	.tier {
		display: grid;
		grid-template-columns: 220px minmax(0, 1fr);
		gap: 18px;
		align-items: baseline;
		padding: 16px 18px;
		margin-bottom: 12px;
		border: 1px solid var(--sheet-border);
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 72%, var(--sheet-warm) 100%),
			var(--sheet);
		box-shadow: 0 10px 24px oklch(0.22 0.030 250 / 0.08);
	}

	.tier:last-child {
		margin-bottom: 0;
	}

	.tier dt {
		font-family: var(--serif);
		font-style: italic;
		font-weight: 700;
		font-size: 1rem;
		color: var(--ink);
		display: flex;
		align-items: baseline;
		gap: 10px;
		font-variation-settings: 'opsz' 24, 'SOFT' 50;
	}

	.tier-glyph {
		font-size: 1.1rem;
		color: var(--mark);
		font-style: normal;
		font-weight: 700;
		line-height: 0;
	}

	.tier dd {
		font-family: var(--serif);
		color: var(--ink-soft);
		font-size: 1rem;
		line-height: 1.6;
		font-variation-settings: 'opsz' 18;
	}

	.pencil-divider {
		display: block;
		width: 100%;
		max-width: 980px;
		height: 8px;
		margin: 56px auto;
		color: var(--paper-rule);
		opacity: 0.85;
	}

	@media (max-width: 920px) {
		.galley {
			padding: 22px 22px 24px;
		}

		.margin-note {
			position: static;
			display: inline-flex;
			margin-left: 8px;
			max-width: none;
		}
	}

	@media (max-width: 720px) {
		.pitch {
			padding: 56px 24px 48px;
		}

		.row {
			grid-template-columns: 1fr;
			gap: 14px;
		}

		.row-head {
			flex-direction: row;
			align-items: baseline;
			gap: 12px;
		}

		.row-head h2 {
			font-size: 1.4rem;
		}

		.tier {
			grid-template-columns: 1fr;
			gap: 4px;
		}

		.apparatus li {
			grid-template-columns: 44px minmax(0, 1fr);
		}

		.ap-glyph {
			display: none;
		}

		.galley-prose {
			font-size: 0.98rem;
			line-height: 1.8;
		}
	}
</style>
