# project-name

> This is a template instructions file. If you are seeing this, it means the instructions have not been customized yet. Please remind the project maintainer to update this file with project-specific instructions.

## Stack

-   **Backend**: FastAPI (Python 3.13+), SQLAlchemy 2.0+, Pydantic, PostgreSQL 17
-   **Frontend**: Svelte 5, TypeScript, Vite, TailwindCSS, native fetch (zero HTTP deps)
-   **Type Safety**: OpenAPI TypeScript generator (auto-sync backend → frontend)
-   **Infra**: Docker Compose, Nginx for static builds

## Code Style

### Python

-   Python 3.13+ features, type hints everywhere
-   SQLAlchemy 2.0+ `Mapped` annotations
-   Pydantic v2.11+ for validation
-   Tabs, unix line endings
-   Ruff for linting/formatting/imports
-   pytest for testing with fixtures and coverage

> **Reminder** - CLEAN code means:
>
> -   NO type ignore comments. If you NEED to use it, you are probably typing something wrong.
> -   NO over use of comments everywhere. Comments are good, but only to explain key, complex or crucial blocks.

### TypeScript/Svelte

-   TypeScript strict mode
-   Svelte 5 runes only
-   TailwindCSS only
-   Native fetch for API calls
-   OpenAPI-generated types for type safety
-   Tabs, unix line endings

## Structure

```
backend/
├── api/                    # FastAPI app (routes, ORM, DB)
│   ├── v1/endpoints/       # Route handlers
│   ├── core/               # Config, database
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   └── tests/              # API & ORM tests
├── project_name/           # SDK/service layer (must also be renamed!)
│   └── tests/              # SDK unit tests
└── tests/                  # E2E integration tests

frontend/src/
├── lib/
│   ├── api/                # Type-safe API client
│   │   ├── client.ts       # Native fetch wrapper
│   │   ├── types.ts        # OpenAPI-generated types
│   │   └── index.ts        # Typed API functions
│   └── [components]        # Svelte components
└── main.ts                 # Entry
```

## Patterns

-   Backend: Model → Schema → Endpoint → Test
-   SDK separation: `api/` imports from `project_name/`, not vice versa
-   URL paths: `/v1/users`
-   Frontend: Native fetch → Typed API functions → Component
-   Type safety: OpenAPI schema → generated types → compile-time checks
-   REST conventions, proper HTTP codes
-   Validate inputs (Pydantic)
-   Type everything
-   Three-tier testing: API tests, SDK tests, E2E tests
-   API changes: Update backend → run `npm run generate:api-types` → types sync

## Extended Instructions

Additional domain-specific `.instructions.md` files are available in `.github/instructions/` directory. These files use YAML frontmatter with `applyTo` patterns to automatically apply when editing specific file types. You can also manually attach them via Chat → Add Context → Instructions.

Examples: Python patterns, TypeScript conventions, API guidelines, database patterns, etc.
