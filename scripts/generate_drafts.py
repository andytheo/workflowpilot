"""Generate editorial outlines using only the Python standard library."""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "drafts"
OUT.mkdir(exist_ok=True)
with (ROOT / "content" / "calendar.csv").open(encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))
for row in rows:
    slug = re.sub(r"[^a-z0-9]+", "-", row["topic"].lower()).strip("-")
    outline = f"""# {row['topic']}

Status: DRAFT — fact-check and human review required
Search intent: {row['search_intent']}
Product category: {row['product_category']}

## Reader problem
[Describe the actual reader problem.]

## Demonstration
[Add tested steps, screenshots and limitations.]

## Options and tradeoffs
[Verify current features, prices and policies using official sources.]

## Recommendation
[Explain who each tool suits. Disclose affiliate relationships.]

## Call to action
{row['cta']}

## Short video
Hook: [Concrete problem]
Demo: [Verified workflow]
Limitation: [Honest tradeoff]
CTA: {row['cta']}

## Caption
[Takeaway, link destination and disclosure if relevant.]
"""
    (OUT / f"{row['id']}-{slug}.md").write_text(outline, encoding="utf-8")
print(f"Generated {len(rows)} editorial outlines")
