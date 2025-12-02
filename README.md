<div align="center">

<img src="https://nokodo.net/media/images/logo_full.svg" alt="nokodo logo" width="320" />
<div style="height:32px"></div>

---

<h1>Monorepo Template</h1>

**Modern & production-ready full-stack template that saves you weeks of setup: FastAPI backend + Svelte 5 frontend with containerization, full CI/CD, VS Code support, and AI integrations.**

[![License](https://img.shields.io/github/license/nokodo-labs/monorepo-template)](LICENSE)
[![Stars](https://img.shields.io/github/stars/nokodo-labs/monorepo-template?style=social)](https://github.com/nokodo-labs/monorepo-template/stargazers)
[![Issues](https://img.shields.io/github/issues/nokodo-labs/monorepo-template)](https://github.com/nokodo-labs/monorepo-template/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/nokodo-labs/monorepo-template)](https://github.com/nokodo-labs/monorepo-template/pulls)
[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Node](https://img.shields.io/badge/node-24+-green.svg)](https://nodejs.org/)

</div>

## 🛠️ Stack

-   **Backend**: FastAPI (Python 3.13+), SQLAlchemy 2.0+, Pydantic, PostgreSQL 17, Alembic, uv
-   **Frontend**: Svelte 5, Vite 6, Tailwind 4, TypeScript, native fetch (zero HTTP deps)
-   **Type Safety**: OpenAPI TypeScript generator (auto-sync backend → frontend types)
-   **Dev**: VS Code (tasks, debugger, extensions), Ruff, pytest, AI instructions
-   **Deploy**: Docker Compose with production configs

## ✨ Features

-   ⚡ **Opinionated by design**: Deliberate choices, cohesive stack, no decision fatigue
-   🏗️ **Production infrastructure**: PostgreSQL 17, multi-stage Docker builds, Nginx configs
-   🔒 **End-to-end type safety**: Python type hints → OpenAPI → auto-generated TypeScript types
-   🤖 **Full CI/CD pipeline**: Automated testing, Docker builds, GHCR publishing, releases
-   🧪 **Complete test setup**: pytest (backend) + Vitest (frontend) with fixtures and full coverage
-   📐 **Modern code standards**: EditorConfig, Ruff, ESLint, Prettier pre-configured
-   💾 **Persistent data storage**: Volume-mounted data directory
-   🛠️ **VS Code integration**: Tasks, debugger configs, recommended extensions
-   🤖 **AI agents ready**: Premade instructions & prompts with extensible patterns
-   🎯 **Minimal boilerplate**: No business logic, just a working foundation
-   🔮 **Future-proof stack**: Latest stable versions of everything, zero tech debt from day one

## 🚀 Quick Start

### 1️⃣ Create Your Repository

-   Click **"Use this template"** on GitHub → Create your repo
-   Clone your new repository locally

### 2️⃣ Customize Project

Rename `backend/project_slug/` to your project name and update references. See [docs/setup.md](docs/setup.md#initial-customization-required) for detailed instructions.

### 3️⃣ Start Development

```bash
cd .docker
docker compose up -d
```

**Your services:**

-   Frontend: http://localhost
-   Backend API: http://localhost:8000
-   API Docs: http://localhost:8000/v1/docs

> 💡 **VS Code users**: Open the workspace to get tasks, debugger configs, and recommended extensions automatically.

### 4️⃣ Deploy to Production

CI/CD automatically builds and pushes Docker images to **GitHub Container Registry (GHCR)** on every commit. Images are tagged as:

-   `ghcr.io/your-org/your-repo:latest` → production branch
-   `ghcr.io/your-org/your-repo:dev` → dev branch
-   `ghcr.io/your-org/your-repo:v1.2.3` → releases

**Deploy with Docker:**

```bash
# Pull pre-built images and deploy
docker compose pull
docker compose up -d
```

> 💡 **Tip**: See [docs/setup.md](docs/setup.md#production-deployment) for full deployment instructions and environment configuration.

## 📁 Structure

```
backend/
├── api/                   # FastAPI application
│   ├── api/v1/endpoints/  # Route handlers
│   ├── core/              # Config, database
│   ├── models/            # SQLAlchemy ORM
│   ├── schemas/           # Pydantic validation
│   ├── tests/             # API & ORM tests
│   └── alembic/           # Database migrations
├── project_slug/          # SDK/service layer (rename me!)
│   └── tests/             # SDK unit tests (optional)
├── tests/                 # E2E integration tests
└── data/                  # Data storage (volume mounted)

frontend/
├── src/
│   ├── lib/               # Components
│   └── main.ts            # Entry point
└── nginx.conf             # Production server

.docker/                   # Docker configs
├── Dockerfile.backend     # Backend build
├── Dockerfile.frontend    # Frontend build
├── docker-compose.yml     # Production
└── docker-compose.dev.yml # Development

.github/                   # CI/CD, Dependabot, CODEOWNERS
.vscode/                   # Editor config, tasks, debugger
tools/release_please/      # Release automation config
```

### 🏗️ Architecture

**Backend:**

-   **`api/`**: FastAPI app, routes, ORM, database setup
-   **`project_slug/`**: Business logic SDK that can be packaged separately for pip/uv/PyPI distribution
-   **Testing**: 3 tiers (API tests in `api/tests/`, SDK tests in `project_slug/tests/`, E2E in `tests/`)
-   **URLs**: `/v1/users` (no `/api` prefix - deploy on `api.yourdomain.com`)

**Frontend:**

-   **Native fetch** - Zero HTTP library dependencies, uses web standards
-   **OpenAPI types** - Auto-generated TypeScript types from FastAPI schema
-   **Type safety** - Backend changes = compile errors in frontend if incompatible

## 📄 License

BSD 3-Clause - See [LICENSE](LICENSE) for details.
