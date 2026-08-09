# project-title Backend

## Tech Stack

-   **Runtime**: Python 3.13+, FastAPI, SQLAlchemy 2.0+, Pydantic v2.11+
-   **Database**: PostgreSQL 17, Alembic migrations
-   **Testing**: pytest with fixtures and coverage
-   **Tooling**: Ruff for linting/formatting/imports

## Code Style

-   Python 3.13+ features, type hints everywhere
-   SQLAlchemy 2.0+ `Mapped` annotations
-   Pydantic v2.11+ for validation
-   Tabs, unix line endings

> **Reminder** - CLEAN code means:
>
> 1.  NO type ignore comments. If you NEED to use it, you are probably typing something wrong.
> 2.  NO overuse of comments everywhere. Comments are good, but only to explain complex or crucial blocks.
> 3.  NO pragma nocs to skip tests. If you need to skip a test, update the test to cover the case, or remove unreachable code instead.
> 4.  NO use of getattr/setattr/delattr unless it's the only way. It defeats type checkers and is ugly.
> 5.  AVOID direct cast() usage. Use only when it's the only way.
> 6.  AVOID use of Any type. Only use when absolutely necessary.
> 7.  Patterns 1, 4, 5 and 6 can be used to **bypass typing issues**, which is **strictly forbidden**.

## Backend Codebase Map

```
backend/
├── api/                    # FastAPI app (routes, ORM, DB)
│   ├── v1/					# v1 API routers, service layer
│   ├── core/               # Config, database
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   └── tests/              # API & ORM tests
├── project_slug/           # SDK/service layer (must also be renamed!)
│   └── tests/              # SDK unit tests
└── tests/                  # E2E integration tests
```

## Patterns

-   Backend: Model → Schema → Endpoint → Test
-   SDK separation: `api/` imports from `project_slug/`, not vice versa
-   URL paths: `/v1/users`
-   REST conventions, proper HTTP codes
-   Validate inputs (Pydantic)
-   Type everything
-   Three-tier testing: API tests, SDK tests, E2E tests
-   API changes: Update backend → run `npm run generate:api-types` → types sync

## Running Backend Code

### About Dev Servers

-   Always assume the user is already running a dev server with hot reload.
-   Always assume the user is monitoring changes live.
-   Never manually run dev servers like `uvicorn` yourself - unless explicitly asked.

### To Run Tests

The simplest way to run all tests is by using the VSCode Task `Backend: Run Tests`.

To run backend tests manually instead:

1.  Always remember to cd into `backend/`
2.  (Optional) Install requirements with `uv sync --all-extras`
3.  Run `uv run pytest` from within the `backend/` directory.
