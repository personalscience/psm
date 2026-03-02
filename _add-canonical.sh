#!/bin/bash
# Post-render script for SEO fixes:
# 1. Inject canonical link tags into all HTML pages
# 2. Remove PDF/EPUB/DOCX entries from sitemap.xml
# 3. Copy llms.txt and generate llms-full.txt

SITE_URL="https://psm.personalscience.com"
OUTPUT_DIR="docs"

# --- Canonical tags ---
find "$OUTPUT_DIR" -name "*.html" -type f | while read -r file; do
  rel_path="${file#$OUTPUT_DIR/}"
  canonical_path=$(echo "$rel_path" | sed 's|/index\.html$|/|; s|^index\.html$||')
  canonical_url="${SITE_URL}/${canonical_path}"
  sed "s|</head>|<link rel=\"canonical\" href=\"${canonical_url}\" />\n</head>|" "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
done

# --- Strip non-HTML entries from sitemap ---
SITEMAP="$OUTPUT_DIR/sitemap.xml"
if [ -f "$SITEMAP" ]; then
  python3 -c "
import re, sys
xml = open('$SITEMAP').read()
xml = re.sub(r'\s*<url>\s*<loc>[^<]*\.(pdf|epub|docx)</loc>.*?</url>', '', xml, flags=re.DOTALL)
open('$SITEMAP', 'w').write(xml)
"
fi

# --- LLMs.txt files ---
cp llms.txt "$OUTPUT_DIR/llms.txt" 2>/dev/null || true
python3 _build-llms-full.py 2>/dev/null || true

# --- Add llms.txt to sitemap ---
if [ -f "$SITEMAP" ]; then
  DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ" 2>/dev/null || date -Iseconds)
  sed "s|</urlset>|  <url>\n    <loc>${SITE_URL}/llms.txt</loc>\n    <lastmod>${DATE}</lastmod>\n  </url>\n</urlset>|" "$SITEMAP" > "${SITEMAP}.tmp" && mv "${SITEMAP}.tmp" "$SITEMAP"
fi
