# Setup

## Quick Start

```bash
cd .docker
docker compose up -d
```

Access:

-   Frontend: http://localhost:5173
-   Backend: http://localhost:8000
-   API Docs: http://localhost:8000/v1/docs

## Local Development

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
pip install -e .[dev]
cp .env.example .env
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env

# Generate API types (requires backend running)
npm run generate:api-types

npm run dev
```

**Type Generation**: Run `npm run generate:api-types` whenever backend API changes to sync TypeScript types.

### Database Only

```bash
cd .docker
docker compose up db -d
```

## VS Code

1. Install recommended extensions
2. Select Python interpreter: `./backend/.venv/bin/python`
3. Use tasks (Ctrl+Shift+P → "Tasks: Run Task")

## Testing

```bash
# Backend
cd backend
pytest -v
pytest --cov=app tests/

# Frontend
cd frontend
npm run test
```

## Docker Commands

```bash
cd .docker

# Start/stop
docker compose up -d
docker compose down
docker compose down -v  # Delete volumes

# Logs
docker compose logs -f [service]

# Rebuild
docker compose up -d --build
```

## Database Migrations

```bash
cd backend
alembic revision --autogenerate -m "Description"
alembic upgrade head
alembic downgrade -1
```

## Production Build

```bash
cd .docker
docker compose build
docker compose up -d
```

Frontend served via Nginx on http://localhost

## Environment Variables

### backend/.env

```
DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/app_db
DEBUG=True
SECRET_KEY=change-in-production
```

### frontend/.env

```
VITE_API_URL=http://localhost:8000/v1
```

## Troubleshooting

**Port conflicts**: Change ports in `.docker/docker-compose.yml`

**DB connection failed**: `docker compose restart db`

**Python imports**: Ensure `PYTHONPATH=./backend` (VS Code sets automatically)

**Module not found**: Delete `node_modules`, run `npm install`
