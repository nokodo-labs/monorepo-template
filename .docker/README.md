# Docker Configuration

## Usage

```bash
# Start all services
docker compose up -d

# Dev mode (hot reload)
docker compose --profile dev up

# Stop
docker compose down

# Remove volumes
docker compose down -v
```

## Services

-   **db**: PostgreSQL 17 (port 5432)
-   **backend**: FastAPI (port 8000)
-   **frontend**: Nginx static build (port 80)

## Configuration

Edit environment variables in `docker-compose.yml`:

-   Database credentials
-   Secret key (MUST change in production)
-   CORS origins
-   Debug mode
