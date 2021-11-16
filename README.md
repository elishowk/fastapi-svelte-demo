# Demo Project

## Frontend

It's build with [`create-svelte`](https://github.com/sveltejs/kit/tree/master/packages/create-svelte);
SvelteKit along with TailwindCSS are used for this demo.


### Developing

Once you've cloned this project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

### API endpoints

We use [SvelteKit Endpoints](https://kit.svelte.dev/docs#routing-endpoints) for backend API fetching. Endpoints in SvelteKit are files ending with .js (or .ts for typescript) that export functions corresponding to HTTP methods. These endpoint files become API routes in our application.

### Building

Before creating a production version of your app, install an [adapter](https://kit.svelte.dev/docs#adapters) for your target environment. Then:

```bash
npm run build
```

> You can preview the built app with `npm run preview`, regardless of whether you installed an adapter. This should _not_ be used to serve your app in production.
