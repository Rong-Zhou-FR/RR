# AGENTS.md — Root Project Rules for RR (Robotika Ron)

This is the canonical, repo-wide instruction file for AI agents working on **RR (Robotika Ron)**.

## Hierarchical Context Model

Agents **must** follow this rule:

> When working inside a directory, load the nearest `AGENTS.md` file and merge it with parent `AGENTS.md` files up to root.
> Local rules override global rules.

Context resolution order (highest priority first):
1. `AGENTS-[module].md` in module directories — module-specific context
2. `AGENTS.md` in current working directory (if present)
3. Root `AGENTS.md` — global project rules

---

## Project Overview

**RR (Robotika Ron)** is a text generation AI agent designed to write text in Rong's style for various scenarios including tech guides, code documentation, emails, and `.enc` encyclopedia entries.

**Core Goals**:
- Working AI agent with public OpenAI-style API
- Reliable reproduction of author's writing style
- Easily modifiable system prompt + scenario-based context injection
- 100% FOSS stack with provider-agnostic design
- Modular, lightweight, and minimalist architecture

**Target Audience**:
- Developers integrating RR into their workflows
- Users generating styled text via API
- Contributors extending RR with new scenarios

---

## Language and Naming Conventions

### Python
- **Style**: PEP 8 compliant
- **Naming**:
  - `snake_case` for functions, variables, modules, packages
  - `PascalCase` for classes, exceptions
  - `UPPER_SNAKE_CASE` for constants
- **Imports**: Standard library → Third-party → Local modules (alphabetically sorted)
- **Docstrings**: Google-style for public functions/classes

### File Naming
- Modules: `snake_case.py` (e.g., `prompt_engine.py`)
- Tests: `test_*.py` (e.g., `test_prompt_engine.py`)
- Config: `*.yaml` or `*.yml` (e.g., `config.yaml`)
- Data: `*.yaml` for styles, `*.enc` for encyclopedia entries

### Git Branch Naming
- `feature/<description>` for new features
- `fix/<description>` for bug fixes
- `docs/<description>` for documentation updates
- `chore/<description>` for maintenance tasks

---

## Tech Stack

### Core Stack (MVP)
- **Framework**: FastAPI (async, auto OpenAPI docs)
- **Model Provider**: Hugging Face Inference API (no local GPU needed)
- **Data Validation**: Pydantic
- **Config/Style Storage**: YAML files
- **Environment**: Python 3.10+

### Optional Stack (Future)
- **Local Models**: Hugging Face Transformers + PyTorch
- **Quantization**: GGUF/GPTQ for smaller footprint
- **Deployment**: Docker + Hugging Face Spaces

### API Format
- OpenAI-compatible request/response format
- Streaming support for long generations

---

## Dependency Management

This project uses **Poetry** for dependency management and packaging.

### Installation
```bash
poetry install
```

### Adding Dependencies
```bash
poetry add <package>
poetry add --group dev <package>  # for dev dependencies
```

### Running Commands
```bash
poetry run <command>
```

---

## Coding Guidelines

1. **Modularity** — Each function does one small thing and one thing only
2. **Provider Agnostic** — Design for easy switching between HF Inference API and local models
3. **Minimal Dependencies** — Import existing FOSS libraries instead of rewriting
4. **Type Hints** — Use type hints for all function signatures
5. **Error Handling** — Graceful error handling with meaningful messages
6. **Testing** — Write tests for all public functions
7. **Documentation** — Document public APIs with docstrings

---

## Documentation Standards

- **Every module must have a corresponding `AGENTS-[module].md` file.**
- **Every command must have documentation in `docs/man/[command].md`.**
- **Help text must include concrete examples.**
- **Options with restricted values MUST document all valid values.**

Format: `Example: --language fr` or `Example: -n 30,80`

---

## Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` — New features
- `fix:` — Bug fixes
- `docs:` — Documentation changes
- `chore:` — Maintenance tasks
- `test:` — Test changes
- `refactor:` — Code refactoring

Format: `<type>: <description>`

Examples:
- `feat: add style selection endpoint`
- `fix: handle HF API rate limiting`
- `docs: update API documentation`

---

## What to Avoid

- **Do not use** deprecated libraries or frameworks
- **Do not add** unnecessary dependencies (keep requirements.txt minimal)
- **Do not** mix business logic with presentation logic
- **Do not** hardcode configuration values (use environment variables)
- **Do not** commit secrets or API keys to the repository
- **Do not** use global variables for state management

---

## Module-Level AGENTS Files

The following module-specific AGENTS files are located in their respective directories:

| Module | AGENTS File | Documentation |
|--------|-------------|---------------|
| API | `app/api/AGENTS-api.md` | `docs/man/api.md` |
| Core | `app/core/AGENTS-core.md` | `docs/man/core.md` |
| Models | `app/models/AGENTS-models.md` | `docs/man/models.md` |
| Services | `app/services/AGENTS-services.md` | `docs/man/services.md` |
| Data | `data/AGENTS-data.md` | `docs/man/data.md` |

(Update this table as new modules are added)

---

## Dependency and Inheritance Map

```
Root AGENTS.md (global rules)
    │
    ├── app/api/AGENTS-api.md (API-specific rules)
    │   └── app/api/v1/AGENTS-v1.md (v1 API rules)
    │
    ├── app/core/AGENTS-core.md (core logic rules)
    │
    ├── app/models/AGENTS-models.md (model provider rules)
    │
    ├── app/services/AGENTS-services.md (service layer rules)
    │
    └── data/AGENTS-data.md (data management rules)
```

Local rules override global rules. Module-level files focus on domain-specific behavior, constraints, and invariants.

---

## Quick Start for Agents

When working on RR:

1. **Read root AGENTS.md** (this file) for global rules
2. **Load nearest AGENTS.md** in current directory
3. **Follow module-specific rules** from AGENTS-[module].md files
4. **Check docs/man/** for command documentation
5. **Run tests** before committing changes
6. **Use Poetry** for dependency management

---

## Project Structure Reference

```
RR/
├── app/                    # Application code
│   ├── api/               # API endpoints and routing
│   ├── core/              # Core logic (prompt engine, style manager)
│   ├── models/            # Model providers (HF Inference API, etc.)
│   ├── schemas/           # Pydantic schemas
│   └── services/          # Business logic services
├── data/                  # Style examples and prompts
│   ├── styles/           # Writing style examples by scenario
│   └── prompts/          # Prompt templates
├── tests/                 # Test suite
├── docs/                  # Documentation
│   └── man/              # Command documentation
├── dev/                   # Development files
│   ├── plans/            # Implementation plans
│   └── AI-prompts/       # AI prompts for development
├── AGENTS.md             # This file (root rules)
├── pyproject.toml        # Poetry configuration
├── README.md             # Human-readable overview
└── .gitignore            # Git ignore rules
```
