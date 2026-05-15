<script>
	import { base } from '$app/paths';

	let scrolled = $state(false);

	function handleScroll() {
		scrolled = window.scrollY > 20;
	}
</script>

<svelte:window onscroll={handleScroll} />

<nav class:scrolled>
	<div class="nav-inner">
		<a href="{base}/" class="wordmark">
			<span class="wordmark-glyph" aria-hidden="true">✓</span>
			<span class="wordmark-text">unsloppify</span>
			<span class="wordmark-meta">v0.1</span>
		</a>
		<div class="nav-links">
			<a href="#rules" class="nav-link">
				<span class="nav-num">i.</span>
				Rules
			</a>
			<a href="#install" class="nav-link">
				<span class="nav-num">ii.</span>
				Install
			</a>
			<a
				href="https://github.com/petems/unsloppify"
				target="_blank"
				rel="noopener noreferrer"
				class="nav-link"
			>
				<span class="nav-num">iii.</span>
				GitHub
			</a>
		</div>
	</div>
</nav>

<style>
	nav {
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 100;
		padding: 16px 32px;
		transition: background 0.3s, box-shadow 0.3s, border-color 0.3s;
		border-bottom: 1px solid transparent;
		background: oklch(0.985 0.004 96 / 0.72);
		backdrop-filter: blur(10px) saturate(120%);
		-webkit-backdrop-filter: blur(10px) saturate(120%);
	}

	nav.scrolled {
		background: oklch(0.985 0.004 96 / 0.94);
		border-bottom-color: var(--paper-rule);
		box-shadow: 0 8px 28px oklch(0.22 0.020 250 / 0.08);
	}

	.nav-inner {
		max-width: var(--col-wide);
		margin: 0 auto;
		display: flex;
		align-items: baseline;
		justify-content: space-between;
	}

	.wordmark {
		display: inline-flex;
		align-items: baseline;
		gap: 8px;
		font-family: var(--mono);
		font-size: 0.92rem;
		font-weight: 600;
		color: var(--ink);
		text-decoration: none;
		letter-spacing: 0;
	}

	.wordmark:hover {
		color: var(--ink);
		text-decoration: none;
	}

	.wordmark-glyph {
		color: var(--mark);
		font-family: var(--mono);
		font-style: normal;
		font-size: 0.95rem;
		font-weight: 700;
		line-height: 0;
		transform: translateY(1px);
	}

	.wordmark-text {
		font-weight: 700;
	}

	.wordmark-meta {
		font-family: var(--mono);
		font-size: 0.72rem;
		color: var(--ink-faint);
		font-weight: 500;
		letter-spacing: 0;
		border: 1px solid var(--paper-rule);
		padding: 1px 5px;
	}

	.nav-links {
		display: flex;
		gap: 22px;
		align-items: baseline;
	}

	.nav-link {
		display: inline-flex;
		align-items: baseline;
		gap: 6px;
		font-family: var(--sans);
		font-size: 0.86rem;
		font-weight: 700;
		color: var(--ink-soft);
		text-decoration: none;
		padding: 4px 0;
		border-bottom: 2px solid transparent;
		transition: color 0.15s, border-color 0.15s;
	}

	.nav-link:hover {
		color: var(--ink);
		border-bottom-color: var(--mark);
		text-decoration: none;
	}

	.nav-num {
		font-family: var(--serif);
		font-style: italic;
		font-size: 0.78rem;
		color: var(--pencil);
	}

	@media (max-width: 560px) {
		nav {
			padding: 12px 20px;
		}

		.wordmark-meta {
			display: none;
		}

		.nav-links {
			gap: 14px;
		}

		.nav-num {
			display: none;
		}
	}
</style>
