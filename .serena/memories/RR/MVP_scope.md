# RR MVP Scope

## Style System
For MVP, focus on **tech_content** only (tech_guides, code_docs). Do not expand emails or encyclopedia scenarios - the blog content is primarily tech-focused and extracting "encyclopedia" or "emails" from it is not representative of actual writing styles.

## Current Status
- tech_guides: 28 examples ✓
- code_docs: 18 examples ✓
- Total: 46 clean tech-focused examples
- Sufficient for RAG implementation (issue #4)

## SDK Decision
- No official client library for MVP
- API is OpenAI-compatible - users can use any OpenAI-compatible client
- Simple API (1 endpoint, 7 fields) doesn't warrant SDK maintenance burden
- Let users use their preferred tools (curl, requests, OpenAI SDK, etc.)