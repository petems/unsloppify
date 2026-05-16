<footer>
	<div class="footer-inner">
		<div class="colophon">
			<div class="colophon-mark" aria-hidden="true">
				<span class="cm-glyph">⌐</span>
				<span class="cm-glyph">∧</span>
				<span class="cm-glyph">¶</span>
			</div>
			<p class="colophon-text">
				Set in <em>Fraunces</em>, <em>Inter</em>, and
				<em>JetBrains&nbsp;Mono</em>. Marked up in OKLCH.<br />
				Built by
				<a href="https://github.com/petems" target="_blank" rel="noopener noreferrer">Peter Souter</a>.
				<span class="mit">&nbsp;·&nbsp; MIT</span>
			</p>
		</div>
		<div class="links">
			<a href="https://github.com/petems/unsloppify" target="_blank" rel="noopener noreferrer">GitHub</a>
			<a href="https://pypi.org/project/unsloppify/" target="_blank" rel="noopener noreferrer">PyPI</a>
			<a href="#install">Install</a>
		</div>
	</div>
	<div class="footer-rule" aria-hidden="true">
		<svg viewBox="0 0 1200 12" preserveAspectRatio="none">
			<path d="M 0 6 Q 150 3, 300 6 T 600 5 T 900 7 T 1200 5" stroke="currentColor" stroke-width="1.2" fill="none" />
		</svg>
		<span class="footer-folio">fin.</span>
	</div>
</footer>

<style>
	footer {
		max-width: var(--col-wide);
		margin: 0 auto;
		padding: 56px 32px 36px;
		position: relative;
	}

	.footer-inner {
		display: grid;
		grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr);
		gap: 40px;
		align-items: end;
		padding-top: 28px;
		border-top: 2px solid var(--ink);
		padding-bottom: 28px;
	}

	.colophon {
		display: flex;
		gap: 18px;
		align-items: flex-start;
	}

	.colophon-mark {
		display: flex;
		flex-direction: column;
		gap: 2px;
		font-family: var(--serif);
		font-style: italic;
		color: var(--mark);
		line-height: 1;
		padding-top: 4px;
	}

	.cm-glyph {
		font-size: 1.1rem;
		opacity: 0.85;
	}

	.cm-glyph:nth-child(2) {
		font-family: var(--mono);
		font-style: normal;
		font-weight: 700;
		font-size: 0.9rem;
		color: var(--pencil);
	}

	.colophon-text {
		font-family: var(--serif);
		font-style: italic;
		font-size: 0.92rem;
		color: var(--ink-muted);
		line-height: 1.55;
		font-variation-settings: 'opsz' 22;
	}

	.colophon-text em {
		font-weight: 700;
		font-style: italic;
		color: var(--ink);
	}

	.colophon-text a {
		color: var(--ink);
	}

	.mit {
		font-family: var(--mono);
		font-style: normal;
		font-size: 0.82em;
		color: var(--ink-faint);
		letter-spacing: 0.04em;
	}

	.links {
		display: flex;
		gap: 22px;
		justify-content: flex-end;
		align-items: baseline;
		font-family: var(--sans);
		font-size: 0.86rem;
	}

	.links a {
		color: var(--ink-soft);
		text-decoration: none;
		border-bottom: 1.5px solid transparent;
		padding-bottom: 2px;
		transition: color 0.15s, border-color 0.15s;
	}

	.links a:hover {
		color: var(--ink);
		border-bottom-color: var(--mark);
	}

	.footer-rule {
		display: flex;
		align-items: baseline;
		gap: 14px;
		color: var(--paper-rule);
	}

	.footer-rule svg {
		flex: 1;
		height: 6px;
	}

	.footer-folio {
		font-family: var(--serif);
		font-style: italic;
		font-size: 0.86rem;
		color: var(--ink-faint);
		letter-spacing: 0.04em;
	}

	@media (max-width: 600px) {
		.footer-inner {
			grid-template-columns: 1fr;
			gap: 18px;
			align-items: flex-start;
		}

		.links {
			justify-content: flex-start;
		}
	}
</style>
