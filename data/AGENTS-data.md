# AGENTS-data.md — Data Module Agent Instructions

## Summary
Data module manages writing style examples, prompt templates, and configuration data for RR.

## Purpose and Expected Behavior
- **Style Examples**: Store writing style examples by scenario
- **Prompt Templates**: Reusable prompt templates for different scenarios
- **Configuration**: Environment-specific configuration files

## Constraints and Invariants
- All style files must be valid YAML
- Style examples must be representative of target writing style
- Never commit API keys or secrets to data files
- Use version control for style changes

## Input/Output Expectations
- **Style Files**: YAML format with name, examples, description
- **Prompt Templates**: Text files with placeholder variables
- **Config Files**: YAML/ENV format with validated structure

## Documentation Reference
- YAML spec: https://yaml.org/spec/
- Git LFS for large files: https://git-lfs.com/

## Domain-Specific Rules for Agents

### Style File Structure
Each style file in `data/styles/{scenario}/` must follow this structure:

```yaml
name: "tech_guide_style"
description: "Rong's tech guide writing style"
examples:
  - "Example text 1..."
  - "Example text 2..."
```

### Scenario Directories
- `data/styles/tech_guides/`: Tech guide style examples
- `data/styles/code_docs/`: Code documentation style examples
- `data/styles/emails/`: Email style examples
- `data/styles/encyclopedia/`: Encyclopedia entry style examples

### Prompt Templates
- Store in `data/prompts/`
- Use `{variable}` syntax for placeholders
- Include scenario-specific instructions
- Keep templates concise and focused

### Adding New Styles
1. Create YAML file in appropriate scenario directory
2. Include 3-5 representative examples
3. Test with prompt engine
4. Commit with descriptive message

### Module Files
- `data/styles/`: Writing style examples by scenario
- `data/prompts/`: Prompt templates
