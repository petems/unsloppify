<script>
	let copied = $state('');

	async function copy(text, id) {
		await navigator.clipboard.writeText(text);
		copied = id;
		setTimeout(() => (copied = ''), 2000);
	}
</script>

<section class="install-section" id="install">
	<div class="install-inner">
		<div class="folio-bar">
			<span class="eyebrow">distribution &nbsp;·&nbsp; install</span>
			<span class="folio">p. 04</span>
		</div>

		<h2>
			<span class="sigil">§ VI.</span>
			Install
		</h2>

		<p class="install-lede">
			One CLI, one Claude Code Plugin or Agentic Skill, one output-style.
			Pick the rail that suits your pipeline.
		</p>

		<div class="methods">
			<div class="method">
				<div class="method-head">
					<span class="method-num">01</span>
					<h3>One-shot CLI</h3>
					<em class="rec">recommended</em>
				</div>
				<p>Try it instantly with no install. Requires <code>uv</code>.</p>
				<div class="cmd">
					<span class="cmd-prompt">$</span>
					<code>uvx unsloppify draft.md</code>
					<button onclick={() => copy('uvx unsloppify draft.md', 'uvx')}>
						{copied === 'uvx' ? 'copied' : 'copy'}
					</button>
				</div>
			</div>

			<div class="method">
				<div class="method-head">
					<span class="method-num">02</span>
					<h3>Persistent CLI</h3>
				</div>
				<p>Install once with pipx, then call <code>unsloppify</code> from anywhere.</p>
				<div class="cmd">
					<span class="cmd-prompt">$</span>
					<code>pipx install unsloppify</code>
					<button onclick={() => copy('pipx install unsloppify', 'pipx')}>
						{copied === 'pipx' ? 'copied' : 'copy'}
					</button>
				</div>
			</div>

			<div class="method">
				<div class="method-head">
					<span class="method-num">03</span>
					<h3>Claude Code plugin</h3>
				</div>
				<p>Adds the <code>/unsloppify</code> skill and the <code>unsloppified</code> output-style.</p>
				<div class="cmd">
					<span class="cmd-prompt">/</span>
					<code>plugin marketplace add petems/unsloppify</code>
					<button onclick={() => copy('/plugin marketplace add petems/unsloppify', 'plugin')}>
						{copied === 'plugin' ? 'copied' : 'copy'}
					</button>
				</div>
				<div class="cmd">
					<span class="cmd-prompt">/</span>
					<code>plugin install unsloppify@unsloppify</code>
					<button onclick={() => copy('/plugin install unsloppify@unsloppify', 'plugin-install')}>
						{copied === 'plugin-install' ? 'copied' : 'copy'}
					</button>
				</div>
			</div>

			<div class="method">
				<div class="method-head">
					<span class="method-num">04</span>
					<h3>Agent Skills</h3>
				</div>
				<p>Works with Claude Code, Codex, Cursor, and any other agent supporting <a href="https://agentskills.io" target="_blank" rel="noopener noreferrer">Agent Skills</a>.</p>
				<div class="cmd">
					<span class="cmd-prompt">$</span>
					<code>npx skills add petems/unsloppify</code>
					<button onclick={() => copy('npx skills add petems/unsloppify', 'skills')}>
						{copied === 'skills' ? 'copied' : 'copy'}
					</button>
				</div>
			</div>

			<div class="method">
				<div class="method-head">
					<span class="method-num">05</span>
					<h3>Pre-commit</h3>
				</div>
				<p>Block slop from ever landing in <code>git</code>.</p>
				<div class="cmd block">
					<span class="cmd-prompt">~</span>
					<code>repos:
  - repo: https://github.com/petems/unsloppify
    rev: v0.1.0
    hooks:
      - id: unsloppify</code>
					<button onclick={() => copy('repos:\n  - repo: https://github.com/petems/unsloppify\n    rev: v0.1.0\n    hooks:\n      - id: unsloppify', 'precommit')}>
						{copied === 'precommit' ? 'copied' : 'copy'}
					</button>
				</div>
			</div>

			<div class="method">
				<div class="method-head">
					<span class="method-num">06</span>
					<h3>GitHub Actions</h3>
				</div>
				<p>Render findings as inline PR annotations with the GitHub reporter.</p>
				<div class="cmd block">
					<span class="cmd-prompt">~</span>
					<code>name: prose
on: [pull_request]
jobs:
  unsloppify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: uvx unsloppify docs/ --format github</code>
					<button onclick={() => copy('name: prose\non: [pull_request]\njobs:\n  unsloppify:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: uvx unsloppify docs/ --format github', 'github-actions')}>
						{copied === 'github-actions' ? 'copied' : 'copy'}
					</button>
				</div>
			</div>
		</div>

		<figure class="github-preview" aria-labelledby="github-preview-title">
			<figcaption id="github-preview-title">
				<span class="preview-kicker">GitHub annotation preview</span>
				<strong>How findings appear on a pull request</strong>
			</figcaption>
			<div class="github-window">
				<div class="github-toolbar">
					<span class="dot red"></span>
					<span class="dot yellow"></span>
					<span class="dot green"></span>
					<span class="github-path">docs/release-notes.md</span>
				</div>
				<div class="github-file">
					<div class="diff-row">
						<span class="line-num">12</span>
						<p>
							<span class="diff-plus">+</span>
							In today's fast-paced world, teams need a seamless way to review copy.
						</p>
					</div>
					<div class="annotation error">
						<div class="annotation-icon" aria-hidden="true">!</div>
						<div>
							<strong>unsloppify opener.today_fast_paced</strong>
							<p>Formulaic opener. Remove the throat-clearing phrase.</p>
						</div>
					</div>
					<div class="annotation warning">
						<div class="annotation-icon" aria-hidden="true">!</div>
						<div>
							<strong>unsloppify vocabulary.seamless</strong>
							<p>AI-coded vocabulary. Replace it with the concrete behavior you mean.</p>
						</div>
					</div>
				</div>
			</div>
		</figure>

	</div>
</section>

<style>
	.install-section {
		background: var(--ink-deep);
		padding: 80px 32px 88px;
		color: var(--ink-deep-text);
		position: relative;
		overflow: hidden;
	}

	.install-section::before {
		content: '';
		position: absolute;
		inset: 0;
		background:
			repeating-linear-gradient(
				to bottom,
				transparent,
				transparent 31px,
				oklch(0.30 0.034 248 / 0.42) 31px,
				oklch(0.30 0.034 248 / 0.42) 32px
			),
			linear-gradient(
				90deg,
				transparent,
				transparent 95px,
				oklch(0.54 0.105 224 / 0.25) 96px,
				transparent 97px
			);
		pointer-events: none;
		opacity: 0.72;
	}

	.install-inner {
		max-width: var(--col-wide);
		margin: 0 auto;
		position: relative;
	}

	.folio-bar {
		display: flex;
		justify-content: space-between;
		align-items: baseline;
		padding-bottom: 14px;
		margin-bottom: 48px;
		border-bottom: 1px solid oklch(0.30 0.012 252);
	}

	.folio-bar .eyebrow {
		color: var(--ink-deep-muted);
	}

	.folio-bar .folio {
		color: var(--ink-deep-muted);
	}

	h2 {
		font-family: var(--serif);
		font-size: 2.2rem;
		font-weight: 900;
		color: oklch(0.96 0.012 80);
		letter-spacing: 0;
		margin-bottom: 14px;
		display: flex;
		align-items: baseline;
		gap: 14px;
		font-variation-settings: 'opsz' 96;
	}

	h2 .sigil {
		font-family: var(--serif);
		font-style: italic;
		font-weight: 400;
		color: var(--mark);
		font-size: 1.4rem;
	}

	.install-lede {
		font-family: var(--serif);
		font-size: 1.1rem;
		color: var(--ink-soft);
		max-width: var(--col-wide);
		width: 100%;
		margin-bottom: 44px;
		font-style: italic;
		line-height: 1.55;
		padding: 20px 24px;
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 70%, var(--sheet-blue) 100%),
			var(--sheet);
		border: 1px solid var(--sheet-border);
		border-left: 5px solid var(--mark);
		box-shadow: 0 16px 34px oklch(0.06 0.020 250 / 0.28);
		position: relative;
		font-variation-settings: 'opsz' 22;
	}

	.install-lede::before {
		content: '';
		position: absolute;
		inset: -1px auto -1px -1px;
		width: 5px;
		background: linear-gradient(var(--mark), var(--pencil));
	}

	.methods {
		display: grid;
		grid-template-columns: repeat(2, minmax(0, 1fr));
		gap: 28px 32px;
		max-width: var(--col-wide);
		width: 100%;
	}

	.method {
		padding: 22px 24px 24px;
		background: oklch(0.22 0.032 250);
		border: 1px solid oklch(0.34 0.042 252);
		position: relative;
		border-radius: 4px;
		min-width: 0;
	}

	.method::before {
		content: '';
		position: absolute;
		top: -1px;
		left: -1px;
		width: 14px;
		height: 14px;
		border-top: 2px solid var(--mark);
		border-left: 2px solid var(--mark);
	}

	.method-head {
		display: flex;
		align-items: baseline;
		gap: 12px;
		margin-bottom: 8px;
	}

	.method-num {
		font-family: var(--mono);
		font-size: 0.78rem;
		color: var(--mark);
		font-weight: 600;
		letter-spacing: 0.04em;
	}

	h3 {
		font-family: var(--serif);
		font-style: italic;
		font-size: 1.18rem;
		font-weight: 700;
		color: oklch(0.96 0.012 80);
		margin: 0;
		font-variation-settings: 'opsz' 36;
	}

	.rec {
		font-family: var(--serif);
		font-style: italic;
		font-size: 0.78rem;
		color: oklch(0.78 0.13 90);
		margin-left: auto;
		letter-spacing: 0.02em;
	}

	.method p {
		font-family: var(--serif);
		color: var(--ink-deep-muted);
		font-size: 0.96rem;
		margin-bottom: 14px;
		line-height: 1.55;
		font-variation-settings: 'opsz' 18;
	}

	.method p a {
		color: oklch(0.78 0.06 245);
		text-decoration-color: oklch(0.55 0.10 245);
	}

	.method p a:hover {
		color: oklch(0.86 0.04 245);
	}

	.method p code {
		font-size: 0.82em;
		background: oklch(0.28 0.014 252);
		color: var(--ink-deep-text);
		border-color: oklch(0.35 0.014 252);
	}

	.cmd {
		display: flex;
		align-items: center;
		gap: 12px;
		background: oklch(0.16 0.014 250);
		border: 1px solid oklch(0.34 0.042 252);
		padding: 12px 14px;
		margin-bottom: 8px;
		font-family: var(--mono);
		position: relative;
		border-radius: 3px;
	}

	.cmd:last-child {
		margin-bottom: 0;
	}

	.cmd.block {
		align-items: flex-start;
	}

	.cmd-prompt {
		font-family: var(--mono);
		color: var(--mark);
		font-weight: 600;
		font-size: 0.85rem;
		line-height: 1.6;
		flex-shrink: 0;
		user-select: none;
	}

	.cmd code {
		font-family: var(--mono);
		font-size: 0.85rem;
		color: oklch(0.92 0.012 80);
		background: transparent;
		padding: 0;
		border: 0;
		flex: 1;
		min-width: 0;
		white-space: pre-wrap;
		overflow-wrap: anywhere;
	}

	.cmd button {
		flex-shrink: 0;
		background: transparent;
		border: 1px solid oklch(0.35 0.014 252);
		color: var(--ink-deep-muted);
		cursor: pointer;
		padding: 4px 12px;
		font-family: var(--mono);
		font-size: 0.7rem;
		letter-spacing: 0.05em;
		text-transform: uppercase;
		font-weight: 600;
		transition: color 0.15s, background 0.15s, border-color 0.15s;
	}

	.cmd button:hover {
		color: oklch(0.97 0.012 80);
		background: oklch(0.28 0.014 252);
		border-color: var(--mark);
	}

	.github-preview {
		margin-top: 34px;
		padding: 24px;
		background:
			linear-gradient(135deg, var(--sheet) 0%, var(--sheet) 70%, var(--sheet-blue) 100%),
			var(--sheet);
		border: 1px solid var(--sheet-border);
		border-left: 5px solid var(--mark);
		box-shadow: 0 16px 34px oklch(0.06 0.020 250 / 0.28);
		position: relative;
	}

	.github-preview::before {
		content: '';
		position: absolute;
		inset: -1px auto -1px -1px;
		width: 5px;
		background: linear-gradient(var(--mark), var(--pencil));
	}

	.github-preview figcaption {
		display: flex;
		justify-content: space-between;
		gap: 18px;
		align-items: baseline;
		margin-bottom: 18px;
		color: var(--ink);
	}

	.preview-kicker {
		font-family: var(--mono);
		font-size: 0.7rem;
		color: var(--ink-muted);
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.github-preview figcaption strong {
		font-family: var(--serif);
		font-size: 1.2rem;
		font-style: italic;
		color: var(--ink);
		font-variation-settings: 'opsz' 36;
	}

	.github-window {
		overflow: hidden;
		border: 1px solid oklch(0.78 0.028 250);
		border-radius: 6px;
		background: oklch(0.99 0.004 250);
		box-shadow: 0 12px 28px oklch(0.22 0.030 250 / 0.12);
	}

	.github-toolbar {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 10px 14px;
		background: oklch(0.95 0.008 250);
		border-bottom: 1px solid oklch(0.82 0.026 250);
	}

	.dot {
		width: 9px;
		height: 9px;
		border-radius: 50%;
	}

	.dot.red { background: var(--mark); }
	.dot.yellow { background: var(--stet); }
	.dot.green { background: var(--verify); }

	.github-path {
		margin-left: 8px;
		font-family: var(--mono);
		font-size: 0.78rem;
		color: var(--ink-muted);
	}

	.github-file {
		padding: 18px;
		background: white;
	}

	.diff-row {
		display: grid;
		grid-template-columns: 42px minmax(0, 1fr);
		gap: 12px;
		align-items: baseline;
		padding: 10px 12px;
		background: oklch(0.96 0.024 150);
		border: 1px solid oklch(0.84 0.055 150);
		font-family: var(--mono);
		font-size: 0.82rem;
		color: var(--ink);
	}

	.line-num {
		color: var(--ink-faint);
		text-align: right;
		user-select: none;
	}

	.diff-plus {
		color: var(--verify);
		font-weight: 700;
		margin-right: 8px;
	}

	.annotation {
		display: grid;
		grid-template-columns: 28px minmax(0, 1fr);
		gap: 12px;
		margin: 12px 0 0 54px;
		padding: 12px 14px;
		border: 1px solid oklch(0.82 0.060 45);
		border-left: 4px solid var(--mark);
		border-radius: 6px;
		background: oklch(0.985 0.010 75);
		color: var(--ink);
	}

	.annotation.warning {
		border-color: oklch(0.82 0.075 90);
		border-left-color: oklch(0.72 0.13 82);
		background: oklch(0.985 0.018 88);
	}

	.annotation-icon {
		width: 22px;
		height: 22px;
		border-radius: 50%;
		background: var(--mark);
		color: white;
		display: grid;
		place-items: center;
		font-family: var(--mono);
		font-size: 0.78rem;
		font-weight: 700;
	}

	.annotation.warning .annotation-icon {
		background: oklch(0.72 0.13 82);
		color: var(--ink);
	}

	.annotation strong {
		display: block;
		font-family: var(--mono);
		font-size: 0.78rem;
		color: var(--ink);
		margin-bottom: 3px;
	}

	.annotation p {
		margin: 0;
		font-family: var(--sans);
		font-size: 0.9rem;
		line-height: 1.45;
		color: var(--ink-soft);
	}

	@media (max-width: 820px) {
		.methods {
			grid-template-columns: 1fr;
			gap: 22px;
		}
	}

	@media (max-width: 600px) {
		.install-section {
			padding: 56px 22px 64px;
		}

		.method {
			padding: 20px 18px 22px;
			overflow: hidden;
		}

		.method-head {
			flex-wrap: wrap;
			gap: 8px 10px;
		}

		.rec {
			margin-left: 0;
		}

		.cmd {
			display: grid;
			grid-template-columns: auto minmax(0, 1fr);
			gap: 8px 10px;
		}

		.cmd code {
			font-size: 0.78rem;
			min-width: 0;
			white-space: pre-wrap;
			word-break: break-word;
		}

		.cmd button {
			grid-column: 1 / -1;
			justify-self: start;
		}

		.github-preview {
			padding: 20px 18px;
		}

		.github-preview figcaption {
			display: block;
		}

		.github-preview figcaption strong {
			display: block;
			margin-top: 6px;
			font-size: 1.08rem;
		}

		.github-file {
			padding: 12px;
		}

		.diff-row {
			grid-template-columns: 28px minmax(0, 1fr);
			font-size: 0.72rem;
			padding: 9px 8px;
		}

		.annotation {
			margin-left: 0;
			grid-template-columns: 24px minmax(0, 1fr);
			padding: 11px 12px;
		}
	}
</style>
