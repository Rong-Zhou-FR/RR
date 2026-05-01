#!/usr/bin/env python3
import json
import os
import re

POSTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ronzz_posts.json")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "styles")

def extract_snippets(content, min_len=50, max_len=250):
    sentences = re.split(r'(?<=[.!?])\s+', content)
    snippets = []
    current = ""
    for s in sentences:
        if len(s.strip()) < min_len:
            continue
        if len(current) + len(s) < max_len:
            current = (current + " " + s).strip()
        else:
            if current:
                snippets.append(current)
            current = s.strip()
    if current and len(current) >= min_len:
        snippets.append(current)
    return snippets

def categorize_post(title, tags, content):
    title_lower = title.lower() if title else ""
    tags_str = " ".join(tags).lower() if tags else ""
    content_lower = content[:500].lower()
    
    code_indicators = ['code', '```', 'function', 'def ', 'class ', 'import ', 'const ', 'let ', 'var ', 'api endpoint', 'runtime error', 'syntax']
    tech_indicators = ['cheatsheet', 'config', 'deploy', 'setup', 'install', 'linux', 'bash', 'terminal', 'dns', 'prisma', 'nuxt', 'python', 'customization']
    email_indicators = ['email', 'mail', 'subject', 'recipient', 'send', 'message']
    wiki_indicators = ['guide', 'tutorial', 'explain', 'understanding', 'what is', 'how to', 'introduction', 'overview', 'explain', 'concept']
    french_indicators = ['est un', 'permet de', 'ce que', 'comment', 'pourquoi', 'description']
    
    code_score = sum(1 for i in code_indicators if i in content_lower)
    tech_score = sum(1 for i in tech_indicators if i in tags_str or i in title_lower)
    email_score = sum(1 for i in email_indicators if i in tags_str or i in title_lower)
    wiki_score = sum(1 for i in wiki_indicators if i in title_lower)
    french_score = sum(1 for i in french_indicators if i in content_lower[:1000])
    
    if code_score >= 2:
        return "code_docs"
    if wiki_score >= 1 and 'cheatsheet' not in title_lower:
        return "encyclopedia"
    if email_score >= 1:
        return "emails"
    if tech_score >= 2 or 'cheatsheet' in title_lower or 'config' in title_lower:
        return "tech_guides"
    if french_score >= 2 and len(content) > 1500:
        return "encyclopedia"
    
    return "tech_guides"

with open(POSTS_FILE) as f:
    posts = json.load(f)

scenarios = {"tech_guides": [], "emails": [], "code_docs": [], "encyclopedia": []}

for p in posts:
    if p['title'] in ['Coming soon', 'coming soon']:
        continue
    if len(p['content']) < 300:
        continue
    
    scenario = categorize_post(p['title'], p['tags'], p['content'])
    snippets = extract_snippets(p['content'])
    
    for snippet in snippets[:5]:
        if len(snippet) > 80:
            scenarios[scenario].append(snippet)

for scenario in scenarios:
    examples = scenarios[scenario][:30]
    output_file = os.path.join(OUTPUT_DIR, scenario, "default.yaml")
    
    yaml_content = f'name: "{scenario}_style"\ndescription: "Rong\'s {scenario} writing style"\nexamples:\n'
    for ex in examples:
        escaped = ex.replace('\\', '\\\\').replace('"', '\\"').replace('\n', ' ').replace('\r', '')
        yaml_content += f'  - "{escaped}"\n'
    
    with open(output_file, "w") as f:
        f.write(yaml_content)
    
    print(f"{scenario}: {len(examples)} examples -> {output_file}")

total = sum(len(scenarios[s][:30]) for s in scenarios)
print(f"\nTotal: {total} examples across 4 scenarios")