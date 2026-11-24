# Exam Paper Grader

An agent that reviews handwritten exam papers (PDF or JPG) containing MCQ
and descriptive questions, assigns marks, and records each student's
score to an Excel sheet.

Grading rules:
- **MCQ**: full marks if the selected option matches the answer key, otherwise 0.
- **Descriptive**: marks awarded dynamically against a rubric/model answer —
  partial credit for partially correct answers, full marks only for the best answer.
- **Output**: one row per student per subject in an Excel sheet
  (name, roll number, subject, total marks, per-question breakdown).

## Status

Being built incrementally, one small capability at a time. See
[`docs/plan.md`](docs/plan.md) for the full step-by-step build plan and
[`PROGRESS.md`](PROGRESS.md) for the daily log of what's been done.

**Currently on: Step 0 — validate handwriting transcription accuracy
before building any grading logic on top of it.**

## Project layout

```
exam-paper-grader/
├── samples/      # sample exam papers (PDF/JPG) used for testing — see samples/README.md
├── scripts/      # grading/automation scripts, added as each step is built
├── output/       # generated Excel sheets, JSON results (gitignored, except .gitkeep)
├── docs/         # plan, rubric format notes, design decisions
├── PROGRESS.md   # daily log
└── README.md
```

## Important cautions baked into this project

- The model never self-reports a final total — totals are always
  recomputed in code from per-question marks.
- Grading requires a rubric/model answer as input; the agent does not
  invent grading standards on its own.
- Roll number is the join key across subjects — it is treated as the
  most safety-critical field to get right.
- Excel writes are never done concurrently from parallel workers.
- This repo is public — do not commit real students' papers, names, or
  roll numbers. Use anonymized or synthetic samples only (see `samples/README.md`).
