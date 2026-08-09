# project-title Frontend

## Tech Stack

- TypeScript strict mode
- Svelte 5 runes only
- TailwindCSS for styling
- Native fetch for API calls (zero HTTP deps)
- OpenAPI-generated types for type safety
- Tabs, unix line endings

## Frontend Codebase Map

```
frontend/src/
├── lib/
│   ├── api/                # Type-safe API client
│   │   ├── client.ts       # Native fetch wrapper
│   │   ├── types.ts        # OpenAPI-generated types
│   │   └── index.ts        # Typed API functions
│   └── [components]        # Svelte components
├── main.ts                 # Entry
├── App.svelte              # Main Svelte app
└── app.css                 # Global styles (TailwindCSS)
```

## Patterns

- Native fetch → Typed API functions → Component
- Type safety: OpenAPI schema → generated types → compile-time checks
- Use Svelte 5 runes (`$state`, `$derived`, `$effect`) - no legacy reactive statements

## Dev Environment

- Always cd into `frontend/` when working on frontend code.

### About Dev Servers

- Always assume the user is already running a dev server with hot reload.
- Always assume the user is monitoring changes live.
- Never manually run dev servers like `npm run dev` yourself - unless explicitly asked.

## Testing & Validation

Use VSCode Tasks for validation:

- **Frontend: Check** - Runs `svelte-check` for TypeScript and Svelte type errors
- **Frontend: Run Tests** - Runs vitest unit tests
