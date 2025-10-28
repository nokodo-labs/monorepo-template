# Template Customization Guide

Before using this template for your project, you must customize several key areas.

## Required Customizations

### 1. Project Name & Package

**Backend SDK Package:**

```bash
# Rename the project_name directory
cd backend
mv project_name your-project-slug

# Update imports in Python files
# Search and replace: "from project_name" → "from your_project_slug"
# Search and replace: "import project_name" → "import your_project_slug"
```

**Project Metadata:**

-   `backend/api/core/config.py`: Update `PROJECT_NAME` field
-   `frontend/package.json`: Update `name` field

### 2. Release Configuration

Update all references in `tools/release_please/`:

**Files to modify:**

-   `release-please-manifest.json`
-   `release-please-config.json`
-   `release-please-config.prerelease.json`

**Search and replace:**

-   `"project-name"` → `"your-project-slug"`
-   `"backend/project-name"` → `"backend/your-project-slug"`

### 3. Code Owners

Edit `.github/CODEOWNERS`:

```
# Replace placeholders with your GitHub handles/teams
* @your-github-org/your-team
/backend/ @your-github-org/backend-team
/frontend/ @your-github-org/frontend-team
```

**Format:**

-   Individual: `@username`
-   Team: `@org-name/team-name`
-   Multiple: `path/ @user1 @user2 @org/team`

### 4. Environment Variables

**Backend (`backend/.env`):**

```env
PROJECT_NAME=Your Project Name
SECRET_KEY=generate-strong-key-for-production
DATABASE_URL=postgresql+psycopg://user:pass@host:port/dbname
```

**Frontend (`frontend/.env`):**

```env
VITE_API_URL=http://localhost:8000/v1
```

## Optional Customizations

### GitHub Actions

Workflows are pre-configured but you may want to adjust:

-   `.github/workflows/backend-ci.yml`: Backend testing
-   `.github/workflows/frontend-ci.yml`: Frontend testing
-   `.github/workflows/docker-build-and-deploy.yml`: Docker builds
-   `.github/workflows/release.yml`: Release automation

### Dependabot

Pre-configured in `.github/dependabot.yml` for:

-   Python packages (weekly)
-   npm packages (weekly)
-   GitHub Actions (weekly)
-   Docker images (weekly)

Adjust schedule if needed:

```yaml
schedule:
    interval: "daily" # or "weekly", "monthly"
```

### Docker Configuration

Dockerfiles are in `.docker/`:

-   `Dockerfile.backend`: Python/FastAPI image
-   `Dockerfile.frontend`: Node/Nginx image

Compose files:

-   `docker-compose.yml`: Production setup
-   `docker-compose.dev.yml`: Development overrides

## Verification Checklist

After customization, verify:

-   [ ] `backend/project_name/` renamed to your slug
-   [ ] All Python imports updated
-   [ ] `tools/release_please/*.json` updated
-   [ ] `.github/CODEOWNERS` configured
-   [ ] `PROJECT_NAME` in `backend/api/core/config.py` updated
-   [ ] `frontend/package.json` name updated
-   [ ] Environment files created (`.env`)
-   [ ] Secret keys generated for production
-   [ ] Docker builds successfully: `cd .docker && docker compose build`
-   [ ] Tests pass: `cd backend && pytest`
-   [ ] Frontend builds: `cd frontend && npm run build`

## Quick Replace Script

```bash
#!/bin/bash
# Replace PROJECT-SLUG with your actual project slug

OLD_NAME="project-name"
NEW_NAME="your-project-slug"

# Rename directory
mv backend/project_name backend/${NEW_NAME//-/_}

# Update release configs
find tools/release_please -type f -name "*.json" -exec sed -i "s/$OLD_NAME/$NEW_NAME/g" {} +

# Update Python imports (requires manual review)
find backend -name "*.py" -exec sed -i "s/project_name/${NEW_NAME//-/_}/g" {} +

echo "✅ Automated replacements complete. Please review changes and update:"
echo "   - .github/CODEOWNERS"
echo "   - backend/api/core/config.py (PROJECT_NAME)"
echo "   - frontend/package.json (name)"
```

**Warning:** Review all automated changes before committing!
