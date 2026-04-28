# RR (Robotika Ron)

Text generation AI agent designed to write text in Rong's style for various scenarios including tech guides, code documentation, emails, and `.enc` encyclopedia entries.

## Features

- **OpenAI-style API**: Compatible with OpenAI client libraries
- **Style Reproduction**: Reliable reproduction of author's writing style
- **Scenario Support**: Tech guides, code documentation, emails, encyclopedia entries
- **Provider Agnostic**: Easy switching between Hugging Face Inference API and local models
- **100% FOSS**: Built with free and open-source software

## Quick Start

### Installation

```bash
poetry install
```

### Configuration

Create a `.env` file:

```bash
HF_API_TOKEN=your_hugging_face_token
DEFAULT_MODEL=mistralai/Mistral-7B-Instruct-v0.1
```

### Running the API

```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000` with interactive docs at `http://localhost:8000/docs`.

### API Usage

```bash
curl -X POST "http://localhost:8000/v1/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a tech guide about Python decorators",
    "scenario": "tech_guides",
    "max_tokens": 500
  }'
```

## Project Structure

```
RR/
├── app/                    # Application code
│   ├── api/               # API endpoints and routing
│   ├── core/              # Core logic (prompt engine, style manager)
│   ├── models/            # Model providers
│   ├── schemas/           # Pydantic schemas
│   └── services/          # Business logic services
├── data/                  # Style examples and prompts
│   ├── styles/           # Writing style examples by scenario
│   └── prompts/          # Prompt templates
├── tests/                 # Test suite
├── docs/                  # Documentation
└── dev/                   # Development files
```

## Development

### Running Tests

```bash
poetry run pytest
```

### Code Quality

```bash
poetry run black .
poetry run ruff check .
```

## License

MIT
