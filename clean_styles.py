#!/usr/bin/env python3
"""Clean style examples by filtering out code-heavy snippets."""
import yaml
import re

def is_code_heavy(text):
    """Check if text is mostly code/instructions, not prose style."""
    # Patterns that indicate code rather than style prose
    code_patterns = [
        r'^sudo\s+',  # starts with sudo
        r'^wget\s+',  # wget command
        r'^curl\s+',  # curl command
        r'^apt\s+', r'^apt-get\s+',  # apt commands
        r'^pip\s+', r'^npm\s+', r'^go\s+',  # package managers
        r'^git\s+',  # git commands
        r'^brew\s+', r'^pacman\s+', r'^yum\s+',
        r'\.sh\s', r'\.py\s', r'\.js\s',  # file extensions in command
        r'chmod\s+', r'chown\s+', r'ln\s+',  # linux commands
        r'return\s+\d',  # exit codes
        r'dpkg\s+', r'configure\s+--',  # install/config
        r'\$\{?\w+\}?',  # shell variables
        r'^\s*#!/',  # shebang
        r'^\s*\$\s+',  # prompt
        r'\|.*fzf',  # pipe to fzf
        r'2>/dev/null',  # stderr redirect
        r'&&.*\|\|',  # complex shell logic
        r'```bash', r'```python', r'```shell',  # code blocks
        r'^(\w+:|#\w+)',  # labels like "Install:" or "# Comments"
    ]
    
    # Count how many patterns match
    match_count = sum(1 for p in code_patterns if re.search(p, text, re.MULTILINE | re.IGNORECASE))
    
    # Also check if line starts with code-like pattern (not prose)
    first_line = text.split('\n')[0] if '\n' in text else text
    if re.match(r'^(sudo|wget|curl|apt|pip|npm|git|brew|#!|\$|\[)', first_line.strip()):
        return True
    
    # If many patterns match, likely code
    return match_count >= 2

def clean_examples(examples):
    """Filter out code-heavy examples."""
    cleaned = []
    for ex in examples:
        if is_code_heavy(ex):
            print(f"  FILTERED: {ex[:80]}...")
            continue
        cleaned.append(ex)
    return cleaned

scenarios = ['tech_guides', 'code_docs']
total_before = 0
total_after = 0

for scenario in scenarios:
    filepath = f'data/styles/{scenario}/default.yaml'
    with open(filepath) as f:
        data = yaml.safe_load(f)
    
    examples = data.get('examples', [])
    total_before += len(examples)
    
    cleaned = clean_examples(examples)
    total_after += len(cleaned)
    
    data['examples'] = cleaned
    with open(filepath, 'w') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
    
    print(f"{scenario}: {len(examples)} -> {len(cleaned)} examples")

print(f"\nTotal: {total_before} -> {total_after} examples (filtered {total_before - total_after})")