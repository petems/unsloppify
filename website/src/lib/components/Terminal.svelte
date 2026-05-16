<script>
	import { onMount } from 'svelte';
	import { lines } from '$lib/data/terminal-script.js';

	let visibleLines = $state(0);
	let mounted = $state(false);
	let terminalBody;

	const delays = lines.map((line) => {
		if (line.cls === 'blank') return 80;
		if (line.cls === 'rule') return 700;
		if (line.cls === 'cmd' || line.cls === 'cmd-go') return 600;
		if (line.cls === 'done') return 500;
		if (line.cls === 'summary') return 450;
		if (line.cls === 'label') return 350;
		return 220;
	});

	async function runAnimation() {
		visibleLines = 0;
		for (let i = 0; i < lines.length; i++) {
			await new Promise((r) => setTimeout(r, delays[i]));
			visibleLines = i + 1;
			if (terminalBody) {
				terminalBody.scrollTop = terminalBody.scrollHeight;
			}
		}
		await new Promise((r) => setTimeout(r, 4000));
		if (mounted) runAnimation();
	}

	onMount(() => {
		mounted = true;
		const observer = new IntersectionObserver(
			([entry]) => {
				if (entry.isIntersecting) {
					runAnimation();
					observer.disconnect();
				}
			},
			{ threshold: 0.2 }
		);
		if (terminalBody) observer.observe(terminalBody);
		return () => {
			mounted = false;
			observer.disconnect();
		};
	});
</script>

<div class="terminal" bind:this={terminalBody}>
	{#each lines as line, i}
		{#if i < visibleLines}
			<div class="line {line.cls}">
				{#if line.cls === 'blank'}&nbsp;{:else}{line.text}{/if}
			</div>
		{/if}
	{/each}
	{#if visibleLines > 0}
		<span class="cursor" class:blink={visibleLines >= lines.length}>_</span>
	{/if}
</div>

<style>
	.terminal {
		background: var(--ink-deep);
		border-radius: 4px;
		font-family: var(--mono);
		font-size: 0.78rem;
		line-height: 1.8;
		height: 320px;
		overflow-y: auto;
		scrollbar-width: none;
		color: var(--ink-deep-text);
		padding: 22px 24px;
		border: 1px solid oklch(0.30 0.035 250);
		position: relative;
		box-shadow:
			inset 0 1px 0 oklch(0.35 0.030 250),
			0 18px 42px oklch(0.20 0.030 250 / 0.22);
	}

	.terminal::before {
		content: 'unsloppify draft.md';
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		height: 28px;
		display: flex;
		align-items: center;
		padding-left: 14px;
		background: oklch(0.21 0.032 250);
		border-bottom: 1px solid oklch(0.30 0.035 250);
		color: var(--ink-deep-muted);
		font-size: 0.66rem;
		letter-spacing: 0.02em;
	}

	.terminal::after {
		content: '';
		position: absolute;
		top: 10px;
		right: 12px;
		width: 8px;
		height: 8px;
		border-radius: 50%;
		background: var(--verify);
		box-shadow: -14px 0 0 var(--stet), -28px 0 0 var(--mark);
		pointer-events: none;
	}

	.terminal::-webkit-scrollbar {
		display: none;
	}

	.line {
		white-space: pre;
		animation: lineIn 0.12s ease-out;
	}

	.line:first-child {
		margin-top: 26px;
	}

	@keyframes lineIn {
		from { opacity: 0; }
		to { opacity: 1; }
	}

	.cmd { color: #f0f4ff; font-weight: 600; }
	.cmd-go { color: #7ee68a; font-weight: 600; }
	.dim { color: var(--dark-muted); }
	.label { color: var(--dark-text); font-weight: 500; }
	.err { color: #f5827a; }
	.warn { color: #e6c860; }
	.summary { color: var(--dark-text); font-weight: 500; }
	.fix { color: #a8c8b8; }
	.rule { color: var(--dark-muted); letter-spacing: 0.2em; }
	.cyan { color: #78c8de; }
	.ok { color: #7ee68a; }
	.done { color: #7ee68a; font-weight: 700; }

	.cursor {
		color: var(--dark-text);
		font-weight: 600;
	}

	.cursor.blink {
		animation: blink 1s step-end infinite;
	}

	@keyframes blink {
		50% { opacity: 0; }
	}

	@media (max-width: 900px) {
		.terminal {
			font-size: 0.72rem;
			height: 320px;
			padding: 18px 20px;
		}
	}
</style>
