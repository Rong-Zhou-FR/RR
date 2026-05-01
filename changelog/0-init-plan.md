# Implementation Plan: Using Ronzz.org Content for RR Style Enhancement

**Date**: 2026-05-01
**Status**: Proposed
**Goal**: Extract authentic writing samples from ronzz.org to improve RR's style reproduction

---

## Executive Summary

Ronzz.org is a Ghost-powered blog (50+ articles) written by the same author (Rong Martin-Siebler ZHOU) who owns RR. Content spans tech tutorials, Christian topics, and personal posts. Using this content for style examples is **high-value, low-risk** since the author controls both projects.

**Recommended Approach**: Hybrid — manual curation for immediate quality + RSS automation for ongoing updates.

---

## 1. Content Source Analysis

| Attribute | Details |
|-----------|---------|
| **Platform** | Ghost CMS (API + RSS available) |
| **Articles** | 50+ posts across 5 categories |
| **Languages** | French (majority), English, Chinese |
| **License** | CC BY-NC-ND 4.0 (non-commercial use with attribution) |
| **Owner** | Same person as RR — implied consent |

### Content Categories → RR Scenarios Mapping

| Ronzz.org Category | Content Types | RR Scenario |
|--------------------|---------------|-------------|
| `CS` (12+ articles) | Tech guides, cheatsheets, how-tos | `tech_guides` |
| `Christianity` | Expository, resource lists | `encyclopedia` |
| `La Vie` | Personal narrative, reviews | `emails` or new `blog_posts` |
| `China/政治` | Political commentary | `encyclopedia` (opinion variant) |
| Code articles | fzf, Nuxt, Git, Terminal | `code_docs` |

---

## 2. Extraction Approaches

| Method | Effort | Reliability | Automation | Best For |
|--------|--------|-------------|------------|----------|
| **Manual copy-paste** | High | Highest | None | Initial curation (best quality) |
| **RSS Feed** | Low | High | Full | Bulk import + ongoing updates |
| **Ghost API** | Medium | High | Full | Structured data (requires API key) |
| **Web scraping** | Medium | Medium | Full | Fallback if others unavailable |

**Recommended**: RSS (`https://ronzz.org/rss/`) as primary, Ghost API as upgrade path.

---

## 3. Data Structure Design

### File Organization

```
data/styles/
├── tech_guides/          # Extend with CS articles
│   └── default.yaml
├── encyclopedia/         # Add Christianity + China articles
│   └── default.yaml
├── emails/               # Add La Vie content
│   └── default.yaml
├── code_docs/            # Add code-heavy articles
│   └── default.yaml
└── blog_posts/           # NEW — non-technical blog content
    ├── default.yaml
    └── metadata.yaml     # Source tracking
```

### YAML Format

**`data/styles/blog_posts/default.yaml`** (example):
```yaml
name: "blog_post_style"
description: "Rong's blog post writing style from ronzz.org"
source:
  url: "https://ronzz.org"
  attribution: "CC BY-NC-ND 4.0"
  extraction_date: "2026-05-01"
examples:
  - "Tutorial example capturing Rong's teaching style..."
  - "Opinion piece example capturing personal voice..."
```

**`data/styles/blog_posts/metadata.yaml`**:
```yaml
source_info:
  name: "ronzz.org"
  base_url: "https://ronzz.org"
  license: "CC BY-NC-ND 4.0"
extraction:
  date: "2026-05-01"
  method: "manual + rss_automation"
content_classification:
  by_type:
    tutorial: 15
    opinion: 10
    review: 5
  by_topic:
    - python
    - linux
    - tech
```

### Metadata Fields to Capture

| Field | Purpose |
|-------|---------|
| `source_url` | Link to original article |
| `publish_date` | Original publication date |
| `category` | Content type (tutorial, opinion, etc.) |
| `tags` | Topic tags from original |
| `word_count` | Content length |
| `extraction_date` | When added to RR |
| `ai_assisted` | Boolean — some articles note AI use |

---

## 4. Technical Implementation

### Phase 1: Manual Curation (Immediate)

**Task**: Select 3-5 best examples per scenario from existing articles.

**Steps**:
1. Browse ronzz.org articles by category
2. Extract 2-3 paragraph excerpts per content type
3. Add to appropriate `data/styles/*/default.yaml`
4. Update attribution field

**Time Estimate**: 1-2 hours

### Phase 2: RSS Automation Script

**File**: `scripts/fetch_ronzz_styles.py`

**Dependencies**: `feedparser`, `html2text`, `pyyaml`

**Functionality**:
```
1. Fetch RSS feed from https://ronzz.org/rss/
2. Parse each entry (title, content, categories, date)
3. Clean HTML → plain text using html2text
4. Classify by category → map to RR scenario
5. Extract representative excerpts (first 200 chars)
6. Output YAML fragments or append to existing files
```

**Example Output** (YAML fragment):
```yaml
- source_url: "https://ronzz.org/configure-fzf-in-ranger/"
  publish_date: "2025-12-16"
  category: "tutorial"
  tags: ["fzf", "ranger", "linux"]
  example: "fzf is a fast, open‑source command‑line 'fuzzy finder' tool..."
```

### Phase 3: Ghost API Integration (Future)

- Generate Content API key from Ghost Admin → Settings → Integrations
- Replace RSS with structured JSON API calls
- Enable incremental updates (fetch only new posts)

---

## 5. Ethical & Legal Considerations

| Concern | Resolution |
|---------|-------------|
| **Copyright** | CC BY-NC-ND 4.0 permits non-commercial use with attribution |
| **Author consent** | Same person owns both RR and ronzz.org — implied consent |
| **AI-assisted content** | Some articles note "We used AI" — mark in metadata, prefer non-AI for style fidelity |
| **Attribution** | Add `attribution` field to YAML; include in prompt (optional) |
| **ND clause** | Using short excerpts as style reference is not "material modification" |

**Risk Level**: Low — author is the same person controlling both projects.

---

## 6. Tech/Tool Requirements

| Requirement | Purpose |
|-------------|---------|
| Python 3.10+ | Runtime for extraction scripts |
| `feedparser` | RSS parsing |
| `html2text` | HTML → plain text conversion |
| `pyyaml` | YAML read/write |
| `requests` | HTTP calls (for Ghost API) |

**Install**:
```bash
poetry add feedparser html2text requests
```

---

## 7. Actionable Next Steps

| Step | Owner | Priority | Time |
|------|-------|----------|------|
| 1. Manual: Curate 5 tech_guides examples from CS articles | Human | P0 | 30 min |
| 2. Manual: Curate 3 encyclopedia examples from Christianity | Human | P0 | 20 min |
| 3. Manual: Curate 3 blog_posts examples from La Vie | Human | P1 | 20 min |
| 4. Create `scripts/fetch_ronzz_styles.py` | Refactorer | P1 | 2-4 hrs |
| 5. Add RSS automation to CI (optional) | Architect | P2 | 1 hr |
| 6. Evaluate Ghost API for structured access | Architect | P2 | 1 hr |

---

## 8. Risks & Mitigations

| Risk | Severity | Mitigation |
|------|----------|-------------|
| AI-assisted content dilutes style | Medium | Tag AI articles; prefer organic content |
| Content drift over time | Low | Version-lock examples in git |
| License change | Low | Monitor ronzz.org footer for updates |
| Multi-language confusion | Low | Use English articles for examples; French informs tone |

---

## Summary

Using ronzz.org content is **highly recommended** — it's authentic writing from the same author, maps well to existing RR scenarios, and has clear legal footing (CC BY-NC-ND). Start with manual curation for immediate quality, then build RSS automation for scale.

**Key Decision**: Should manual curation focus on English articles only, or include French for tone/style pattern learning?