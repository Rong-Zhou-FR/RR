# API Documentation

## Overview

The RR API provides an OpenAI-compatible interface for generating text in Rong's style.

## Base URL

```
http://localhost:8000
```

## Endpoints

### Generate Text

**Endpoint**: `POST /v1/generate`

**Request Body**:
```json
{
  "prompt": "Write a tech guide about Python decorators",
  "scenario": "tech_guides",
  "model": "mistralai/Mistral-7B-Instruct-v0.1",
  "max_tokens": 500,
  "temperature": 0.7,
  "top_p": 0.9
}
```

**Response**:
```json
{
  "text": "Generated text in Rong's style...",
  "model": "mistralai/Mistral-7B-Instruct-v0.1",
  "scenario": "tech_guides"
}
```

### Get Style

**Endpoint**: `GET /v1/style/{scenario}`

**Parameters**:
- `scenario` (required): One of `tech_guides`, `code_docs`, `emails`, `encyclopedia`

**Response**:
```json
{
  "name": "tech_guide_style",
  "description": "Rong's tech guide writing style",
  "examples": ["example 1", "example 2"]
}
```

## Scenarios

- `tech_guides`: Technical tutorials and guides
- `code_docs`: Code documentation
- `emails`: Email writing
- `encyclopedia`: Encyclopedia entries

## Error Handling

- `404`: Style not found for scenario
- `422`: Validation error (invalid parameters)
- `500`: Internal server error
