import type { EndpointOutput } from '@sveltejs/kit';

import { variables } from '../lib/variables';
import type { User } from '../lib/types';

const { apiPath } = variables;

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export interface Output<Body extends Record<string, any>> extends EndpointOutput {
	body?: Body;
	ok: boolean;
	error?: string;
}

export async function getWhoami(): Promise<Output<{ user: User }>> {
	const res = await fetch(`${apiPath}/whoami`, {
		headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
	});

	const data: { user: User } = await res.json();
	return { status: res.status, body: data, ok: res.ok };
}

export async function postLogin(
	identifier: string,
	password: string
): Promise<Output<{ user: User; jwt: string }>> {
	const res = await fetch(`${apiPath}/login`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
		body: JSON.stringify({ identifier, password })
	});
	const data = await res.json();

	return { status: res.status, body: data, ok: res.ok };
}

export async function postLogout(): Promise<Output<{ result: boolean }>> {
	const res = await fetch(`${apiPath}/logout`);
	const data = await res.json();

	return { status: res.status, body: data, ok: res.ok };
}
