# RR (Robotika Ron)

Text generation AI agent designed to write text in Rong's style for various scenarios including tech guides, code documentation, emails, and `.enc` encyclopedia entries.

## Features

- **OpenAI-style API**: Compatible with OpenAI client libraries
- **Style Reproduction**: Reliable reproduction of author's writing style
- **Scenario Support**: Tech guides, code documentation (MVP: tech_content only)
- **RAG Support**: Dynamic style example retrieval based on query relevance
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
# Optional: Custom endpoint (for self-hosted or Inference Pro)
# HF_BASE_URL=https://router.huggingface.co/v1/chat/completions
```

### Running the API

```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000` with interactive docs at `http://localhost:8000/docs`.

### API Usage

#### Basic Request (static style injection)
```bash
curl -X POST "http://localhost:8000/v1/generate/" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a tech guide about Python decorators",
    "scenario": "tech_guides",
    "max_tokens": 500
  }'
```

#### With RAG (dynamic retrieval)
```bash
curl -X POST "http://localhost:8000/v1/generate/" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a tech guide about Python decorators",
    "scenario": "tech_guides",
    "use_rag": true,
    "max_tokens": 500
  }'
```

**RAG vs Static:**
- `use_rag: false` (default): All style examples injected (static)
- `use_rag: true`: Top-3 most relevant examples retrieved via embeddings

RAG uses `sentence-transformers/all-MiniLM-L6-v2` for semantic similarity. Recommended for diverse queries.

### OpenAI-Compatible Endpoint

RR exposes an OpenAI-compatible `/v1/chat/completions` endpoint for use with OpenAI client libraries:

```bash
# Using OpenAI client
curl -X POST "http://localhost:8000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "local",
    "messages": [{"role": "user", "content": "Write about Python"}]
  }'
```

This enables RR to be used as a custom model provider in tools like opencode:

```json
// opencode.json example
{
  "provider": {
    "rr": {
      "options": {
        "baseURL": "http://localhost:8000/v1"
      }
    }
  }
}
```

**Configuration:** Set `HF_BASE_URL` in `.env` to use a custom Hugging Face endpoint (e.g., Inference Pro). Default: `https://router.huggingface.co/v1/chat/completions`

## Project Structure

```
RR/
├── app/                    # Application code
│   ├── api/               # API endpoints
│   ├── core/              # Core logic
│   ├── models/            # Model providers
│   ├── schemas/           # Pydantic schemas
│   └── services/          # Business logic
├── data/styles/           # Writing style examples
├── tests/                 # Test suite
└── docs/                  # Documentation
```

## SDK / Client Libraries

**No official SDK for MVP.** RR's API is OpenAI-compatible, so you can use any OpenAI-compatible client:

### Why no SDK?
- Simple API (1 endpoint) — doesn't warrant maintenance burden
- OpenAI SDK works out of the box — just change `base_url`
- Let users use their preferred tools

### Recommended Tools

**CLI/TUI:**
- [httpie](https://httpie.io/) — `http POST localhost:8000/v1/generate/ prompt="..."`
- [curlie](https://github.com/rs/curlie) — curl with the power of httpie
- [Insomnia](https://insomnia.rest/) — GUI HTTP client
- [Postman](https://www.postman.com/) — GUI API testing

**Python:**
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="dummy"  # no auth for local dev
)
response = client.chat.completions.create(
    model="default",
    messages=[{"role": "user", "content": "Your prompt"}]
)
```

**cURL:**
```bash
curl -X POST "http://localhost:8000/v1/generate/" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Your prompt", "scenario": "tech_guides"}'
```

## Contributing

For developer setup, coding standards, and contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
