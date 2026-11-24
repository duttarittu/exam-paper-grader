# Build plan

Building this step by step. Each step must work before moving to the next.

- [x] **Step 0** — Prove handwriting transcription accuracy on sample
  papers before writing any grading logic. Done with synthetic samples
  only (see `docs/step0_result.md`); **real handwriting accuracy is
  still unproven** and should be re-checked once real samples are
  available.
- [x] **Step 1** — Grade one MCQ-only paper, single subject, hardcoded
  answer key. Console output only. Done: `scripts/grade_mcq.py` against
  `samples/sample3_mcq.html`.
- [ ] **Step 2** — Add descriptive-question grading for a single question,
  single paper, against a rubric/model answer provided as input.
- [ ] **Step 3** — Full single paper: mixed MCQ + descriptive, one student,
  extract name/roll number, recompute total in code (never trust a
  model-reported total).
- [ ] **Step 4** — Append one student's result to an Excel sheet using a
  proper spreadsheet-writing tool (not LLM-generated spreadsheet content).
- [ ] **Step 5** — Batch mode: many students, one subject. Sequential (or
  fan-out with serialized Excel writes) processing of a folder of papers.
  Handle duplicates/illegible papers by flagging, not crashing.
- [ ] **Step 6** — Multiple subjects / exam sessions, config-driven
  rubrics and answer keys.
- [ ] **Step 7** — Review/audit layer: flag low-confidence transcriptions
  and borderline grading decisions for human spot-check.

## Standing cautions (apply at every step)

1. Never let the grading model generate the final numeric total — always
   recompute from per-question marks in code.
2. Require rubrics/model answers as explicit input; never let the agent
   invent grading criteria.
3. Treat handwriting transcription as unreliable by default; build in
   confidence flags / human review.
4. Roll number correctness is the integrity backbone of the whole
   system — validate against a roster where possible.
5. Never parallelize Excel writes.
6. This repo is public: never commit real student names, roll numbers,
   or real papers. Use synthetic/anonymized samples only.
