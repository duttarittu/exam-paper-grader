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
- No real handwritten samples were available yet, so added a second,
  harder synthetic sample (`samples/sample2.jpg`) instead: rotated page,
  a struck-through MCQ option with a correction note, a struck-through
  word corrected inline in a descriptive answer, and misspellings
  throughout. Re-ran Step 0 — exact match again, including both tricky
  cases (see `docs/step0_result.md`).
- Real handwritten samples still not available; moved on to Step 1
  using synthetic samples, with the "real accuracy unproven" caveat
  staying open.
- **Switched workflow**: now editing, running, committing and pushing
  directly on the user's Mac (`/Users/rittusmac/Projects/exam-paper-grader`)
  via Remote Control, instead of a separate cloud copy + `git pull`.
  Set a repo-local git identity (`duttarittu <duttarittu@gmail.com>`)
  there so commits work.
- **Step 1 done**: added `samples/sample3_mcq.html` (MCQ-only paper,
  Mathematics, 5 questions x 2 marks = 10) and
  `scripts/grade_mcq.py` — a plain Python grading script with a
  hardcoded answer key and hardcoded "transcribed" student answers.
  Marks are computed entirely in code (never by the model): per-question
  correct/wrong + marks, and a total recomputed by summing, never taken
  as a single reported value. Verified: 4/5 correct, Q5 wrong (selected
  3.16, correct 3.14), **total 8/10**, printed to console.
- Installed Playwright + Chromium as a project dev dependency on the Mac
  (`npm install`) to render sample HTML papers to JPG there going
  forward, since image generation now also needs to happen locally.
