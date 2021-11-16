<script lang="ts">
	import type { User } from '../lib/types';
	import { goto } from '$app/navigation';
	import user from '../lib/user';
	import { postLogin } from './api';

	let email = '';
	let password = '';

	async function login() {
		const res = await postLogin(email, password);
		if (res.ok) {
			const data: { user: User; jwt: string } = res.body;
			localStorage.setItem('token', data.jwt);
			if (data) {
				$user = data.user;
				goto('/');
			}
		} else {
			const { error } = res;
			console.error(`login error`);
			console.log(error);
		}
	}
</script>

<form on:submit|preventDefault={login} class="container mx-auto my-4">
	<h1 class="text-center text-2xl font-bold">Login</h1>

	<div class="my-1">
		<label for="email">Email</label>
		<input type="email" placeholder="Enter your email" bind:value={email} />
	</div>
	<div class="my-1">
		<label for="password">Password</label>
		<input type="password" placeholder="Enter your password" bind:value={password} />
	</div>
	<div class="my-3">
		<button class="submit" type="submit">Login</button>
	</div>
</form>

<style lang="postcss">
	label {
		@apply font-bold block mb-1;
	}

	input {
		@apply bg-white w-full border border-gray-500 rounded outline-none py-2 px-4;
	}

	.submit {
		@apply bg-blue-500 text-white border-transparent rounded px-4 py-2;
	}
</style>
