<script>
	import Terminal from './Terminal.svelte';
</script>

<section class="hero">
	<div class="hero-grid" aria-hidden="true">
		<span></span>
		<span></span>
		<span></span>
	</div>

	<div class="folio-bar">
		<span class="eyebrow">copy desk check · markdown proofing</span>
		<span class="folio">sheet 01</span>
	</div>

	<div class="hero-inner">
		<div class="hero-text">
			<div class="status-strip" aria-label="Proof status">
				<span class="status-dot"></span>
				<span>120+ checks</span>
				<span>regex first</span>
				<span>skill where needed</span>
			</div>

			<h1>
				Proofread the tells before they reach the repo.
			</h1>

			<p class="subtitle">
				<code>unsloppify</code> is a CLI prose linter for markdown. It fixes
				the mechanical AI tells, flags the phrases that need judgment, and
				ships the same standards as a Claude Code skill and output style.
			</p>

			<div class="actions">
				<a href="#install" class="cta">
					<span>Install</span>
					<span class="cta-glyph" aria-hidden="true">→</span>
				</a>
				<a
					href="https://github.com/petems/unsloppify"
					target="_blank"
					rel="noopener noreferrer"
					class="ghost"
				>GitHub</a>
			</div>
		</div>

		<div class="proof-stack">
			<figure class="proof-card">
				<figcaption>
					<span>editorial proof</span>
					<strong>draft.md</strong>
				</figcaption>
				<p>
					<span class="cut">In today's fast-paced world,</span>
					teams need a <span class="cut">seamless</span>
					<span class="insert">clear</span> way to
					<span class="cut">delve into</span>
					<span class="insert">review</span> copy before release.
				</p>
				<div class="margin-notes" aria-hidden="true">
					<span>delete opener</span>
					<span>replace jargon</span>
					<span>keep meaning</span>
				</div>
			</figure>

			<div class="hero-terminal">
				<div class="terminal-tag">
					<span class="terminal-tag-glyph" aria-hidden="true">⌁</span>
					<span>CI trace</span>
				</div>
				<Terminal />
			</div>
		</div>
	</div>
</section>

<style>
	.hero {
		position: relative;
		padding: 96px 32px 54px;
		overflow: hidden;
		isolation: isolate;
	}

	.hero::before {
		content: '';
		position: absolute;
		inset: 0 auto 0 50%;
		width: min(34vw, 430px);
		background: linear-gradient(90deg, transparent, oklch(0.92 0.042 224 / 0.55));
		transform: translateX(128px);
		z-index: -2;
	}

	.hero-grid {
		position: absolute;
		inset: 0;
		max-width: var(--col-wide);
		margin: 0 auto;
		pointer-events: none;
		z-index: -1;
	}

	.hero-grid span {
		position: absolute;
		top: 68px;
		bottom: 42px;
		width: 1px;
		background: oklch(0.84 0.038 224 / 0.68);
	}

	.hero-grid span:nth-child(1) { left: 0; }
	.hero-grid span:nth-child(2) { left: 96px; }
	.hero-grid span:nth-child(3) { right: 0; }

	.folio-bar {
		max-width: var(--col-wide);
		margin: 0 auto 38px;
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		padding-bottom: 14px;
		border-bottom: 1px solid var(--paper-rule);
	}

	.hero-inner {
		max-width: var(--col-wide);
		margin: 0 auto;
		display: grid;
		grid-template-columns: minmax(0, 0.95fr) minmax(360px, 1.05fr);
		gap: 56px;
		align-items: start;
	}

	.hero-text {
		position: relative;
		padding: 24px 28px 28px 28px;
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 68%, var(--sheet-warm) 100%),
			var(--sheet);
		border: 1px solid var(--sheet-border);
		border-left: 4px solid var(--mark);
		box-shadow: var(--sheet-shadow);
	}

	.hero-text::before {
		content: '';
		position: absolute;
		top: -1px;
		bottom: -1px;
		left: 0;
		width: 4px;
		background: linear-gradient(var(--mark), var(--pencil));
	}

	.status-strip {
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
		margin-bottom: 24px;
		font-family: var(--mono);
		font-size: 0.72rem;
		color: var(--ink-muted);
		text-transform: uppercase;
		letter-spacing: 0.06em;
	}

	.status-strip span:not(.status-dot) {
		border: 1px solid var(--paper-rule);
		background: oklch(0.99 0.004 96 / 0.82);
		padding: 4px 8px;
	}

	.status-dot {
		width: 10px;
		height: 10px;
		border-radius: 50%;
		background: var(--verify);
		align-self: center;
		box-shadow: 0 0 0 4px var(--verify-soft);
	}

	h1 {
		font-family: var(--serif);
		font-size: 4.18rem;
		font-weight: 900;
		line-height: 0.98;
		letter-spacing: 0;
		margin-bottom: 28px;
		max-width: 640px;
		font-variation-settings: 'opsz' 144, 'SOFT' 25, 'WONK' 0;
	}

	.subtitle {
		font-size: 1.08rem;
		color: var(--ink-soft);
		line-height: 1.62;
		max-width: 560px;
		margin-bottom: 34px;
	}

	.actions {
		display: flex;
		gap: 18px;
		align-items: center;
	}

	.cta {
		display: inline-flex;
		align-items: center;
		gap: 10px;
		padding: 13px 22px;
		background: var(--ink);
		color: var(--paper);
		border-radius: 3px;
		font-family: var(--sans);
		font-weight: 700;
		font-size: 0.95rem;
		text-decoration: none;
		transition: background 0.18s, transform 0.12s, color 0.18s, box-shadow 0.18s;
		border: 1.5px solid var(--ink);
		box-shadow: 6px 6px 0 var(--pencil);
	}

	.cta:hover {
		background: var(--mark);
		border-color: var(--mark);
		color: white;
		transform: translate(-2px, -2px);
		box-shadow: 8px 8px 0 var(--ink);
		text-decoration: none;
	}

	.cta-glyph {
		font-family: var(--mono);
		transition: transform 0.18s;
	}

	.cta:hover .cta-glyph {
		transform: translateX(3px);
	}

	.ghost {
		font-size: 0.95rem;
		font-weight: 700;
		color: var(--ink-soft);
		text-decoration: none;
		padding: 12px 4px;
		border-bottom: 2px solid var(--paper-rule);
	}

	.ghost:hover {
		color: var(--mark-hot);
		border-bottom-color: var(--mark);
	}

	.proof-stack {
		display: grid;
		gap: 18px;
		min-width: 0;
	}

	.proof-card {
		position: relative;
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 58%, var(--sheet-blue) 100%),
			var(--sheet);
		border: 1px solid var(--sheet-border);
		border-left: 8px solid var(--mark);
		padding: 18px 170px 20px 24px;
		box-shadow:
			10px 10px 0 oklch(0.90 0.035 224),
			var(--sheet-shadow);
	}

	.proof-card figcaption {
		display: flex;
		justify-content: space-between;
		gap: 18px;
		margin-bottom: 12px;
		font-family: var(--mono);
		font-size: 0.72rem;
		color: var(--ink-muted);
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.proof-card figcaption strong {
		color: var(--ink);
		font-weight: 700;
		letter-spacing: 0;
		text-transform: none;
	}

	.proof-card p {
		font-family: var(--serif);
		font-size: 1.28rem;
		line-height: 1.72;
		color: var(--ink);
		font-variation-settings: 'opsz' 28;
	}

	.cut {
		color: var(--ink-faint);
		text-decoration: line-through;
		text-decoration-color: var(--mark);
		text-decoration-thickness: 2px;
		text-decoration-skip-ink: none;
	}

	.insert {
		display: inline-block;
		color: var(--pencil);
		background: var(--pencil-soft);
		padding: 0 5px;
		border-bottom: 2px solid var(--pencil);
		font-style: italic;
	}

	.margin-notes {
		position: absolute;
		top: 58px;
		right: 18px;
		display: grid;
		gap: 10px;
		width: 122px;
		font-family: var(--mono);
		font-size: 0.68rem;
		line-height: 1.35;
		color: var(--mark-hot);
		text-transform: uppercase;
	}

	.margin-notes span {
		border-top: 1px solid var(--mark);
		padding-top: 4px;
	}

	.hero-terminal {
		position: relative;
		min-width: 0;
		padding-top: 8px;
	}

	.terminal-tag {
		display: inline-flex;
		align-items: center;
		gap: 8px;
		font-family: var(--mono);
		font-size: 0.7rem;
		letter-spacing: 0.08em;
		color: var(--ink-muted);
		text-transform: uppercase;
		margin-bottom: 10px;
		padding-left: 4px;
	}

	.terminal-tag-glyph {
		color: var(--pencil);
		font-size: 1rem;
		line-height: 0;
		font-weight: 700;
	}

	@media (max-width: 980px) {
		.hero {
			padding: 86px 24px 52px;
		}

		.folio-bar {
			margin-bottom: 36px;
		}

		.hero-inner {
			grid-template-columns: 1fr;
			gap: 42px;
		}

		h1 {
			font-size: 3.35rem;
		}
	}

	@media (max-width: 620px) {
		.hero {
			padding: 72px 20px 28px;
		}

		.hero-text {
			padding: 20px 18px 22px 18px;
		}

		.folio-bar {
			margin-bottom: 24px;
		}

		.hero-inner {
			gap: 24px;
		}

		.status-strip {
			gap: 6px;
			margin-bottom: 18px;
			font-size: 0.64rem;
		}

		.status-strip span:not(.status-dot) {
			padding: 3px 6px;
		}

		h1 {
			font-size: 2.34rem;
			line-height: 1.02;
			margin-bottom: 20px;
		}

		.subtitle {
			font-size: 0.98rem;
			line-height: 1.55;
			margin-bottom: 22px;
		}

		.proof-card {
			padding: 16px 18px 18px;
			box-shadow: 6px 6px 0 oklch(0.90 0.035 224);
		}

		.proof-card p {
			font-size: 0.96rem;
			line-height: 1.55;
		}

		.margin-notes {
			display: none;
		}

		.actions {
			flex-wrap: wrap;
		}

		.hero-terminal {
			display: none;
		}
	}
</style>
