# Data Module Documentation

## Overview

The data module manages writing style examples, prompt templates, and configuration data for RR.

## Directory Structure

```
data/
├── styles/
│   ├── tech_guides/
│   │   └── default.yaml
│   ├── code_docs/
│   │   └── default.yaml
│   ├── emails/
│   │   └── default.yaml
│   └── encyclopedia/
│       └── default.yaml
└── prompts/
```

## Style Files

Each style file is a YAML file with the following structure:

```yaml
name: "style_name"
description: "Human-readable description"
examples:
  - "Example text 1"
  - "Example text 2"
  - "Example text 3"
```

## Adding New Styles

1. Create a new YAML file in the appropriate scenario directory
2. Include 3-5 representative examples
3. Test with the prompt engine
4. Commit with a descriptive message

## Prompt Templates

Store reusable prompt templates in `data/prompts/`. Use `{variable}` syntax for placeholders.
