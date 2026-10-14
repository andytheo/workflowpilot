# WorkflowPilot

Zero-budget starter for an educational AI-tools and small-business automation affiliate brand.

## Current status
This repository contains a static website, editorial calendar, first video script, and a Python outline generator. No affiliate accounts, sales, or automatic video publishing are connected yet.

## Getting started
1. Enable GitHub Pages: Settings → Pages → Deploy from a branch → main → /(root).
2. Review the site and replace placeholders before promoting it.
3. Run `python scripts/generate_drafts.py` to generate editorial outlines from `content/calendar.csv`.
4. Produce original demos and check every product claim against current official information.
5. Apply to affiliate programs; use approved tracking links and clear affiliate disclosures.

## Free stack
GitHub Pages, GitHub Actions (within usage limits), Python standard library, OBS and a free video editor. Publishing is manual until integrations are validated.

Do not invent product tests, prices, customer results, or income claims. WorkflowPilot is a provisional brand; verify name availability before public launch.


## Get generated scripts and images locally (Windows)

1. Open [Prepare short-form content packs](https://github.com/andytheo/workflowpilot/actions/workflows/production.yml).
2. Click **Run workflow** on the `main` branch. Wait for the green check.
3. Open GitHub Desktop, choose `workflowpilot`, click **Fetch origin**, then **Pull origin** if offered.
4. Open the local repository in Explorer. The `production/` directory contains ten numbered folders. Each folder has `script.md`, `caption.txt`, `storyboard.md`, `review.md` and an `assets/` folder with three vertical cards, a cover and a blog feature graphic.

**Important:** GitHub Desktop does not automatically pull changes without a local scheduled sync. Generated assets are committed to the *public* repository; do not put private information in the production files. This workflow uses `GITHUB_TOKEN` with `contents: write`. If the push fails, check repository Settings → Actions → General → Workflow permissions and ensure the workflow is allowed to write repository contents. Avoid changing these settings without understanding the implications.

These are review-required content templates and static graphics, not completed AI videos. Publishing and affiliate program approval remain separate steps.
