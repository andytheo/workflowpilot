"""Create usable editorial production packs using only the Python standard library.

This is deterministic template-based generation, NOT an AI model or a finished video renderer.
All packs require fact-checking and a human review before publication.
"""
from pathlib import Path
import csv
import json
import re
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "production"
OUT.mkdir(exist_ok=True)

def slugify(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")

with (ROOT / "content" / "calendar.csv").open(encoding="utf-8", newline="") as source:
    topics = list(csv.DictReader(source))

manifest = []
for topic in topics:
    title = topic["topic"]
    folder = OUT / f'{int(topic["id"]):02d}-{slugify(title)}'
    folder.mkdir(parents=True, exist_ok=True)
    steps = [
        ("0:00–0:05", f"Here's a practical question: {title.lower().rstrip('.')}?"),
        ("0:05–0:15", "Start with the problem you want to solve. Show a concrete example rather than a generic promise."),
        ("0:15–0:35", "Demonstrate one verifiable step using your own recording. Add on-screen labels for each action."),
        ("0:35–0:48", "Explain an important limitation, tradeoff, or privacy consideration."),
        ("0:48–0:60", f"If this is useful, see the complete guide for more detail. {topic['cta']}."),
    ]
    script = "# " + title + "\n\n**Status:** Requires human verification and recording.\n\n"
    script += "\n\n".join(f"**{time}** — {line}" for time, line in steps)
    (folder / "script.md").write_text(script + "\n", encoding="utf-8")
    storyboard = "# Storyboard\n\nFormat: vertical 9:16, 1080×1920.\n\n"
    storyboard += "\n".join(f"- {time}: {['Title card with problem','Screenshot of current manual process','Real screen recording of a tested step','Limitation card','Guide link CTA'][i]}" for i,(time,_) in enumerate(steps))
    (folder / "storyboard.md").write_text(storyboard + "\n", encoding="utf-8")
    caption = (f"{title}\n\nA practical workflow, not a magic shortcut. "
               f"See the full guide at https://andytheo.github.io/workflowpilot/guides/ "
               "No paid endorsement or affiliate link in this post. "
               "#Automation #AITools #SmallBusiness")
    (folder / "caption.txt").write_text(caption + "\n", encoding="utf-8")
    checklist = """# Pre-publication review

- [ ] Verify all facts, pricing, features and product terms
- [ ] Record a real demonstration or use licensed visuals
- [ ] Replace template narration with specific and accurate steps
- [ ] Verify video audio, captions, safe areas and export rights
- [ ] Check the destination guide is relevant and live
- [ ] Add clear affiliate disclosures if affiliate links are present
- [ ] Review each platform's rules and schedule manually
- [ ] Record URL, publish date and results in the tracker
"""
    (folder / "review.md").write_text(checklist, encoding="utf-8")
    manifest.append({"topic":title,"folder":str(folder.relative_to(ROOT)),"status":"review_required","created":str(date.today())})
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(f"Created {len(manifest)} short-form production packs in {OUT}")
