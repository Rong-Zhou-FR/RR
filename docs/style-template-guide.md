# Style Template Guide

This guide explains how to create and manage writing style templates for RR (Robotika Ron).

## YAML Structure

Each style file must follow this structure:

```yaml
name: "style_name"
description: "Human-readable description of the style"
examples:
  - "Example text 1"
  - "Example text 2"
  - "Example text 3"
```

### Required Fields

- **name**: Unique identifier for the style (e.g., "tech_guide_style")
- **description**: Human-readable description of the writing style
- **examples**: Array of text examples demonstrating the style

### Optional Fields

- **instructions**: Additional instructions for the AI model
- **keywords**: Important keywords or phrases associated with the style

## Selecting Representative Examples

### Guidelines for Choosing Examples

1. **Clarity**: Choose examples that clearly demonstrate the writing style
2. **Variety**: Include different types of content (paragraphs, lists, code snippets)
3. **Length**: Mix short and long examples to show range
4. **Authenticity**: Use real examples from actual writing when possible
5. **Relevance**: Ensure examples match the target scenario

### Example Selection by Scenario

#### Tech Guides
- Include examples that explain technical concepts clearly
- Show how to break down complex topics
- Demonstrate use of code snippets and technical terminology
- Include examples of step-by-step instructions

#### Code Documentation
- Include examples of function, class, and module documentation
- Show clear parameter descriptions
- Demonstrate return value documentation
- Include examples of inline comments

#### Emails
- Include examples of different email types (requests, updates, thank yous)
- Show professional yet friendly tone
- Demonstrate clear subject lines and call-to-action
- Include examples of both formal and informal emails

#### Encyclopedia Entries
- Include examples that provide factual, informative content
- Show clear definition of concepts
- Demonstrate objective, encyclopedic tone
- Include examples of historical or technical explanations

## Common Pitfalls to Avoid

### 1. Insufficient Examples
- **Problem**: Too few examples don't provide enough context for the AI
- **Solution**: Include at least 3-5 representative examples per style

### 2. Poor Quality Examples
- **Problem**: Low-quality examples lead to poor generation quality
- **Solution**: Carefully review and curate examples before adding them

### 3. Inconsistent Style
- **Problem**: Examples that don't match the target style confuse the AI
- **Solution**: Ensure all examples in a file follow the same style

### 4. Overly Long Examples
- **Problem**: Very long examples can exceed token limits
- **Solution**: Keep examples concise but representative (aim for 1-3 sentences)

### 5. Missing Context
- **Problem**: Examples without context are hard to interpret
- **Solution**: Include brief context in the description field

## Adding New Styles

### Step-by-Step Process

1. **Identify the Scenario**: Determine which scenario the style belongs to
2. **Collect Examples**: Gather 3-5 representative examples
3. **Create YAML File**: Create a new YAML file in the appropriate directory
4. **Test the Style**: Test with the prompt engine to ensure quality
5. **Document**: Update this guide if needed

### Directory Structure

```
data/styles/
├── tech_guides/
│   └── default.yaml
├── code_docs/
│   └── default.yaml
├── emails/
│   └── default.yaml
└── encyclopedia/
    └── default.yaml
```

## Testing Style Templates

### Manual Testing

1. Start the API server
2. Use curl to test generation with the new style
3. Review the output for style consistency
4. Adjust examples as needed

### Automated Testing

Use pytest to verify style loading and prompt construction:

```bash
poetry run pytest tests/test_style_manager.py
poetry run pytest tests/test_prompt_engine.py
```

## Version Control

- Commit style files with descriptive messages
- Use `git diff` to review changes to style examples
- Consider using Git LFS for large style files
- Document major style changes in commit messages

## Troubleshooting

### Style Not Found Error
- Check that the style file exists in the correct directory
- Verify the YAML syntax is valid
- Ensure the scenario name matches the directory name

### Poor Generation Quality
- Review and improve the style examples
- Check that examples are representative of the target style
- Consider adding more examples

### Token Limit Exceeded
- Reduce the number of examples used in prompts
- Shorten individual examples
- Adjust max_tokens parameter in API requests
