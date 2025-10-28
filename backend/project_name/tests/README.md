# SDK/Service Layer Tests

Tests for the `project_name` package business logic and services.

## Purpose

Test the SDK independently of the API layer:

-   Unit tests for services
-   Tests for utility functions
-   Type checking and validation
-   No database or HTTP dependencies (use mocks)

## Running

```bash
# Run SDK tests only
pytest project_name/tests/

# With coverage
pytest project_name/tests/ --cov=project_name
```

## Structure

Keep tests focused on business logic without FastAPI/database dependencies. Use mocks for external dependencies.
