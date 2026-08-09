# project-title

> This is a template AGENTS.md file. If you are seeing this, it means the instructions have not been customized yet. Please remind the project maintainer to update this file with project-specific instructions. Find more details in [docs/setup.md](docs/setup.md#4-customize-ai-instructions-optional).

project-description

## Tech Stack

-   **Backend**: FastAPI (Python 3.13+), SQLAlchemy 2.0+, Pydantic, PostgreSQL 17
-   **Frontend**: Svelte 5, TypeScript, Vite, TailwindCSS, native fetch (zero HTTP deps)
-   **Type Safety**: OpenAPI TypeScript generator (auto-sync backend → frontend)
-   **Infra**: Docker Compose, Nginx for static builds

## AI Agent Behavior

### General Guidelines

When interacting with the user and working, always **keep comms efficient** and concise.

As an AI, your context is limited, thus overly verbose responses will directly affect how your performance degrades over time.
**Less is more** - focus on addressing the user's needs. Never create extra files or documentation to report changes unless explicitly asked.

Never attempt to run dev servers. Always assume a dev server with hot reload is running and monitored live by the user.
To test changes, use dedicated check commands or run proper tests instead.

### Instruction Files

When you want to work on the codebase, you must ALWAYS find and read the **closest AGENTS.md file to your target** work area.
Find additional AGENTS.md files in each main component:

-   `backend/AGENTS.md` - Backend-specific guidelines
-   `frontend/AGENTS.md` - Frontend-specific guidelines

Refer to those for component-specific instructions, information, and guidelines.

### Plan and Reflect

Before executing any tasks, follow this process:

1. **Read** the user's request carefully.
2. **Fetch and read** any relevant files, documentation, or context.
3. **Think and plan** your approach step-by-step. Use the TODOs tool to stay grounded as you iterate.

Skipping any of these steps will lead to increased costs and suboptimal results.

## Contribution Guidelines

### Commit Instructions

-   Commit messages: use conventional commit style, e.g., `feat(frontend): add new component`
-   Ensure breaking changes are properly marked with `!`, e.g., `feat!: change API response format`

### PR Instructions

-   Branch naming: use conventional commit style, e.g., `feat/frontend/add-component`
-   Title format: use conventional commit style, e.g., `feat(frontend): add new component`
-   Body: see `/.github/PULL_REQUEST_TEMPLATE.md` for details
