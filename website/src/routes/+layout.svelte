<script>
	import '../app.css';
	import Nav from '$lib/components/Nav.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<title>unsloppify -- Strip AI slop from your prose</title>
</svelte:head>

<Nav />
{@render children()}
