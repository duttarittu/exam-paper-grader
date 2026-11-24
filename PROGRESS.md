# Progress log

## 2026-11-24
- Set up project repo and folder structure (`samples/`, `scripts/`,
  `output/`, `docs/`).
- Wrote the full build plan (`docs/plan.md`) and standing cautions.
- Attached a folder on the user's Mac (`~/Projects`) via Remote Control
  and cloned the repo there too, so it can be opened in a local editor.
  That's a separate copy — synced only via git push/pull.
- Generated a synthetic handwritten-style sample paper
  (`samples/sample1.html` → `samples/sample1.jpg`, via
  `scripts/generate_sample.js`, rendered with a handwriting web font and
  headless Chromium) with mixed MCQ + descriptive questions, marks, and
  a name/roll header.
- Ran Step 0 transcription check against it — exact match against
  `samples/sample1.expected.md` (see `docs/step0_result.md`).
  **Caveat: this only proves the pipeline works, not real handwriting
  accuracy** — the font is clean/computer-rendered. Still need real
  handwritten samples before trusting this.
- Next: get 2-3 real handwritten samples (messy writing, crossed-out
  MCQ answers, faint pencil) and re-run the Step 0 check for a real
  accuracy number before starting Step 1 (grading logic).
