# GitHub Copilot Instructions

## Stack

-   **Backend**: FastAPI (Python 3.13+), SQLAlchemy 2.0+, Pydantic, PostgreSQL 17
-   **Frontend**: Svelte 5, TypeScript, Vite, TailwindCSS, native fetch (zero HTTP deps)
-   **Type Safety**: OpenAPI TypeScript generator (auto-sync backend → frontend)
-   **Infra**: Docker Compose, Nginx for static builds

## Code Style

### Python

-   Python 3.13+ features, type hints everywhere
-   Async/await for DB operations
-   SQLAlchemy 2.0+ `Mapped` annotations
-   Pydantic for validation
-   100 char lines, tabs, unix line endings
-   Ruff for linting/formatting

### TypeScript/Svelte

-   TypeScript strict mode
-   Svelte 5 runes only (`$state`, `$derived`, `$effect`)
-   TailwindCSS only (no inline styles)
-   Native fetch for API calls (no axios/HTTP libs)
-   OpenAPI-generated types for type safety
-   Tabs, unix line endings

## Structure

```
backend/
├── api/                    # FastAPI app (routes, ORM, DB)
│   ├── api/v1/endpoints/   # Route handlers
│   ├── core/               # Config, database
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   └── tests/              # API & ORM tests
├── project_name/           # SDK/service layer (rename!)
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
-   URL paths: `/v1/users` (no `/api` prefix)
-   Frontend: Native fetch → Typed API functions → Component
-   Type safety: OpenAPI schema → generated types → compile-time checks
-   REST conventions, proper HTTP codes
-   Validate inputs (Pydantic)
-   Type everything
-   Test coverage 80%+
-   Three-tier testing: API tests, SDK tests, E2E tests
-   API changes: Update backend → run `npm run generate:api-types` → types sync

## Extended Instructions

Load from `.github/instructions/` for domain-specific patterns.
