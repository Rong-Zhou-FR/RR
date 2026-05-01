#!/usr/bin/env python3
import requests
import json
import re
from html import unescape
import os

GHOST_URL = "https://ronzz.org"
API_KEY = "22c868e016967e1087b43c7e53"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def fetch_all_posts():
    posts = []
    page = 1
    while True:
        url = f"{GHOST_URL}/ghost/api/content/posts/?key={API_KEY}&include=tags&limit=all&page={page}"
        r = requests.get(url)
        data = r.json()
        posts.extend(data.get('posts', []))
        if not data.get('posts') or len(data.get('posts', [])) < 20:
            break
        page += 1
    return posts

def clean_html(html):
    if not html:
        return ""
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = unescape(text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[\r\n]+', '\n', text)
    text = text.strip()
    return text

posts = fetch_all_posts()

cleaned_posts = []
for p in posts:
    content = clean_html(p.get('html', ''))
    excerpt = clean_html(p.get('excerpt', ''))
    cleaned_posts.append({
        "id": p.get("id"),
        "title": p.get("title"),
        "slug": p.get("slug"),
        "excerpt": excerpt[:500] if excerpt else "",
        "content": content,
        "tags": [t.get("name") for t in p.get('tags', [])],
        "published_at": p.get("published_at")
    })

output_path = os.path.join(OUTPUT_DIR, "ronzz_posts.json")
with open(output_path, "w") as f:
    json.dump(cleaned_posts, f, ensure_ascii=False, indent=2)

print(f"Fetched {len(posts)} posts, saved to {output_path}")