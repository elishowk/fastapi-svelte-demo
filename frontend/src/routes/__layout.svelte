<script lang="ts">
	import { onMount } from 'svelte';
	import '../app.css';
	import userStore from '../lib/user';
	import type { User } from '../lib/types';
	import Navbar from '../lib/components/Navbar.svelte';
	import { getWhoami } from './api';

	let loading = true;

	onMount(async () => {
		// Check if 'token' exists in localStorage
		if (!localStorage.getItem('token')) {
			loading = false;
			return { props: { user: null } };
		}

		// Fetch the user from strapi
		const res = await getWhoami();
		loading = false;
		if (res.ok) {
			const user: User = res.body.user;
			$userStore = user;
		}
	});
</script>

<Navbar />
{#if !loading}
	<slot />
{/if}
