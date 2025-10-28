# Monorepo Template

Modern full-stack boilerplate: FastAPI backend + Svelte 5 frontend with containerization, VS Code support, and AI integrations.

## Stack

-   **Backend**: FastAPI (Python 3.13+), SQLAlchemy 2.0+, Pydantic, PostgreSQL 17, Alembic
-   **Frontend**: Svelte 5, TypeScript, Vite 6, TailwindCSS, native fetch (zero HTTP deps)
-   **Type Safety**: OpenAPI TypeScript generator (auto-sync backend → frontend types)
-   **Dev**: VS Code (tasks, debugger, extensions), Ruff, pytest
-   **Deploy**: Docker Compose with production configs

## Quick Start

```bash
cd .docker
docker compose up -d
```

-   Frontend: http://localhost (Nginx)
-   Backend API: http://localhost:8000
-   API Docs: http://localhost:8000/v1/docs

## Structure

```
backend/
├── api/                   # FastAPI application
│   ├── api/v1/endpoints/  # Route handlers
│   ├── core/              # Config, database
│   ├── models/            # SQLAlchemy ORM
│   ├── schemas/           # Pydantic validation
│   └── tests/             # API & ORM tests
├── project_name/          # SDK/service layer (rename me!)
│   └── tests/             # SDK unit tests (optional)
├── tests/                 # E2E integration tests
├── data/                  # Data storage (volume mounted)
└── alembic/               # Database migrations

frontend/
├── src/
│   ├── lib/               # Components
│   └── main.ts            # Entry point
├── nginx.conf             # Production server
└── Dockerfile             # Multi-stage build

.docker/                   # Docker Compose configs
.vscode/                   # Editor config, tasks, debugger
.github/                   # Copilot instructions
```

### Architecture

**Backend:**

-   **`api/`**: FastAPI app, routes, ORM, database setup
-   **`project_name/`**: Business logic SDK that can be packaged separately for pip distribution
-   **Testing**: 3 tiers (API tests in `api/tests/`, SDK tests in `project_name/tests/`, E2E in `tests/`)
-   **URLs**: `/v1/users` (no `/api` prefix - deploy on `api.yourdomain.com`)

**Frontend:**

-   **Native fetch** - Zero HTTP library dependencies, uses web standards
-   **OpenAPI types** - Auto-generated TypeScript types from FastAPI schema
-   **Type safety** - Backend changes = compile errors in frontend if incompatible

**Rename `project_name`**: Change directory name and update imports when starting a real project.

## Configuration

### Backend (.env)

```env
DATABASE_URL=postgresql+psycopg://user:pass@localhost:5432/db
DEBUG=False
SECRET_KEY=change-in-production
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000/v1
```

### Docker Compose

Edit `.docker/docker-compose.yml`:

-   Database credentials (POSTGRES_PASSWORD)
-   Secret key (SECRET_KEY)
-   CORS origins
-   Ports if conflicts exist

## Local Dev (No Docker)

```bash
# Backend
cd backend
python -m venv .venv && .venv\Scripts\Activate.ps1  # Windows
pip install -e .[dev]
cp .env.example .env
uvicorn api.main:app --reload

# Frontend
cd frontend
npm install
cp .env.example .env
npm run dev
```

## Commands

```bash
# Docker (from .docker/)
docker compose up -d              # Start all
docker compose down               # Stop
docker compose logs -f [service]  # View logs
docker compose down -v            # Remove volumes

# Backend (from backend/)
pytest api/tests/ -v              # Run API tests
pytest --cov=api --cov=project_name tests/  # E2E with coverage
ruff format .                     # Format code
ruff check . --fix                # Lint + autofix
alembic revision --autogenerate   # New migration
alembic upgrade head              # Run migrations

# Frontend (from frontend/)
npm run dev                       # Dev server
npm run build                     # Production build
npm run lint                      # Lint
npm run generate:api-types        # Generate types from backend OpenAPI
```

## VS Code

-   Install recommended extensions (prompt on open)
-   Use tasks: Ctrl+Shift+P → "Tasks: Run Task"
-   Debug: F5 → Choose "Python: FastAPI" or "Frontend: Chrome"

## Features

-   ✅ Python 3.13+, Node 24+ enforced
-   ✅ Full type safety: Python type hints, TypeScript strict, OpenAPI auto-sync
-   ✅ Modern: Native fetch (no axios/HTTP lib deps), Svelte 5 runes, FastAPI
-   ✅ Tabs + unix line endings (editorconfig)
-   ✅ Ruff: format, lint, import sorting
-   ✅ Hot reload: backend + frontend
-   ✅ Data directory: `backend/data/` (volume mounted)
-   ✅ Production ready: multi-stage builds, Nginx
-   ✅ Tests: pytest with async fixtures
-   ✅ Minimal: no business logic, easily customizable
-   ✅ Future-proof: Built on web standards, no legacy dependencies

## What's NOT Included

-   ❌ Makefile (use VS Code tasks or direct commands)
-   ❌ Authentication (add as needed)
-   ❌ Verbose docs (template is minimal by design)

## License

MIT
