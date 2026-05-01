# Contributing to RR (Robotika Ron)

Thank you for your interest in contributing! This guide covers everything you need to know to get started.

## Project Overview

**RR** is a text generation AI agent that writes text in Rong's personal style for various scenarios: tech guides, code documentation, emails, and encyclopedia entries.

- **Status**: MVP complete (v0.1.0), active development
- **Repository**: https://github.com/Rong-Zhou-FR/RR
- **Quick Start**: See README.md for basic installation and API usage

## Prerequisites

- Python 3.10+
- Poetry (for dependency management)
- Hugging Face API token

## Setup

1. **Install dependencies**
   ```bash
   poetry install
   ```

2. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your HF_API_TOKEN
   ```

3. **Verify setup**
   ```bash
   poetry run pytest -v
   ```

## Running the Application

```bash
# Start the API server
poetry run uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs

## Testing

Run the full test suite:
```bash
poetry run pytest -v
```

## Code Quality

### Formatting (Black)
```bash
poetry run black app/ tests/ --check
```

### Linting (Ruff)
```bash
poetry run ruff check app/ tests/ --ignore N818
```

### Configuration
- **Line length**: 88 characters
- **Python version**: 3.10+
- ** Ruff ignores**: N818 (exception naming)

## Coding Standards

- Follow PEP 8
- Use type hints on all function signatures
- Write Google-style docstrings for public APIs
- Use `snake_case` for functions/variables, `PascalCase` for classes
- Module-specific rules in `AGENTS-[module].md` files

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` — New features
- `fix:` — Bug fixes
- `docs:` — Documentation changes
- `chore:` — Maintenance tasks
- `test:` — Test changes
- `refactor:` — Code refactoring

## Documentation

Every module should have a corresponding `AGENTS-[module].md` file. See existing examples in:
- `app/core/AGENTS-core.md`
- `app/api/AGENTS-api.md`
- `data/AGENTS-data.md`

## Need Help?

- Check the README.md for quick start guide
- Review docs/man/ for command documentation
- Explore existing code and tests for patterns
