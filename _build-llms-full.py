#!/usr/bin/env python3
"""Build llms-full.txt from rendered HTML pages.

Extracts main content from each chapter's HTML, strips tags,
and concatenates into a single markdown-like text file.
"""

import html
import os
import re

OUTPUT_DIR = "docs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "llms-full.txt")
SITE_URL = "https://psm.personalscience.com"

# Chapter HTML files in book order
CHAPTERS = [
    ("index.html", "Introduction"),
    ("intro.html", "Getting Started"),
    ("downloads/What is Personal Science.html", "What is Personal Science?"),
    ("science.html", "The Science of the Microbiome"),
    ("Science/microbesEverywhere.html", "Microbes Everywhere"),
    ("downloads/Microbes and You.html", "Microbes and You"),
    ("Science/microbes_in_you.html", "Microbes In You"),
    ("Science/microbes-and-health.html", "Microbes and Health"),
    ("methods.html", "Methods"),
    ("downloads/Handling microbiome data.html", "Handling Microbiome Data"),
    ("downloads/Microbes to Watch.html", "Microbes to Watch"),
    ("Experiments.html", "My Experiments"),
    ("myTests.html", "My Tests"),
    ("CaseStudies.html", "Case Studies"),
    ("downloads/DIY Microbiome Testing.html", "DIY Microbiome Testing"),
    ("downloads/Beyond Bacteria.html", "Beyond Bacteria"),
    ("downloads/Microbes and Genes.html", "Microbes and Genes"),
    ("Next/references-books.html", "Recommended Books"),
    ("Next/references-academic.html", "Academic Papers"),
]


def extract_main_content(html_text):
    """Extract text from the main content area of a Quarto HTML page."""
    # Find the main content div
    main_match = re.search(
        r'<main[^>]*>(.*?)</main>', html_text, re.DOTALL
    )
    if not main_match:
        # Fallback: try the content div
        main_match = re.search(
            r'<div[^>]*id="quarto-content"[^>]*>(.*?)</div>\s*<!-- /main -->',
            html_text, re.DOTALL
        )
    if not main_match:
        return ""

    content = main_match.group(1)

    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    # Remove nav elements (TOC, pagination)
    content = re.sub(r'<nav[^>]*>.*?</nav>', '', content, flags=re.DOTALL)
    # Remove code blocks (R output) but keep figure captions
    content = re.sub(r'<pre[^>]*>.*?</pre>', '', content, flags=re.DOTALL)
    content = re.sub(r'<code[^>]*>.*?</code>', '', content, flags=re.DOTALL)

    # Convert headers to markdown
    for i in range(1, 7):
        hashes = '#' * i
        content = re.sub(
            rf'<h{i}[^>]*>(.*?)</h{i}>',
            lambda m, h=hashes: f'\n\n{h} {_strip_tags(m.group(1)).strip()}\n\n',
            content, flags=re.DOTALL
        )

    # Convert paragraphs to double newlines
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\n\1\n\n', content, flags=re.DOTALL)
    # Convert list items
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', content, flags=re.DOTALL)
    # Convert links
    content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)
    # Convert emphasis
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)

    # Strip remaining HTML tags
    content = _strip_tags(content)
    # Decode HTML entities
    content = html.unescape(content)
    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r' +', ' ', content)

    return content.strip()


def _strip_tags(text):
    """Remove all HTML tags from text."""
    return re.sub(r'<[^>]+>', '', text)


def main():
    header = f"""# Personal Science Guide to the Microbiome

> A practical guide to understanding your microbiome through personal science — covering gut bacteria, 16S rRNA sequencing, self-experiments, and what the latest research means for your health. Written by Richard Sprague, based on 600+ personal microbiome samples collected over several years.

Source: {SITE_URL}

---
"""

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        out.write(header)

        for filename, title in CHAPTERS:
            filepath = os.path.join(OUTPUT_DIR, filename)
            if not os.path.exists(filepath):
                continue

            with open(filepath, 'r', encoding='utf-8') as f:
                html_text = f.read()

            content = extract_main_content(html_text)
            if content:
                out.write(f"\n\n---\n\n")
                out.write(content)

        out.write(f"\n\n---\n\nEnd of document. For the full formatted version visit: {SITE_URL}\n")

    # Report size
    size = os.path.getsize(OUTPUT_FILE)
    print(f"Generated {OUTPUT_FILE}: {size:,} bytes")


if __name__ == "__main__":
    main()
