# Step 0 — transcription accuracy check, sample1.jpg

Method: read `samples/sample1.jpg` directly (vision), transcribe without
looking at `sample1.html` or `sample1.expected.md` first, then diff
against the ground truth.

## What was transcribed from the image

- Name: Ananya Roy
- Roll No: 23
- Subject: General Science, Max Marks: 20
- Q1 [2 marks]: options (a) Oxygen (b) Carbon dioxide (c) Nitrogen
  (d) Hydrogen — circled: **(b) Carbon dioxide**
- Q2 [2 marks]: options (a) 100°C (b) 90°C (c) 120°C (d) 50°C —
  circled: **(a) 100°C**
- Q3 [6 marks]: "When sun light go through small water drops in the air,
  the light bend and split into different colour. This make a rainbow
  shape in the sky. It happen only when sun is behind us and rain drop
  infront."
- Q4 [10 marks]: "The water cycle has three main steps. First,
  evaporation - heat from the sun turns water from oceans, rivers and
  lakes into water vapour which rises into the air. Second, condensation
  - as the vapour rises it cools down and changes back into tiny water
  droplets, forming clouds. Third, precipitation - when the droplets in
  the clouds become heavy enough, they fall back to the earth as rain,
  snow or hail. The water that falls collects in rivers, lakes and
  oceans again, and the whole cycle repeats. This cycle keeps fresh
  water moving around the planet."

## Result

**Exact match against `sample1.expected.md`** — name, roll number, both
circled MCQ options, and both descriptive answers verbatim (grammatical
errors in Q3 preserved, not auto-corrected).

## Caveat — this is not a real accuracy result yet

This sample is a clean, computer-rendered "handwriting" font — it proves
the pipeline (image → vision model → structured transcription) works
end-to-end, but says nothing about accuracy on real handwriting, which
has messier strokes, inconsistent letter formation, cross-outs, faint
pencil, skewed phone photos, and ambiguous circled/crossed MCQ marks.

**Step 0 is not done until this is re-run against a few real handwritten
samples.** Until then, treat transcription reliability as unproven.

## sample2.jpg — messier synthetic sample

No real handwritten samples were available yet, so this sample
deliberately adds harder cases within the synthetic approach: slight
page rotation, a struck-through MCQ option with a correction note
(Q1), a struck-through word corrected inline within a descriptive
answer (Q4: "two" → "three"), and intentional misspellings throughout
Q3/Q4 that must not be auto-corrected.

Transcribed fresh from `samples/sample2.jpg`:
- Name: Test Student, Roll No: 07, Social Studies, Max Marks: 20
- Q1: (a) Jawaharlal Nehru — struck through, with note "← not this one";
  **(b) Dr. Rajendra Prasad — circled** (correctly identified as the
  selected answer, not confused with the struck-through option)
- Q2: **(d) Paris — circled**
- Q3: transcribed verbatim including all misspellings (becuase, wen,
  facs, oposite, nite, contrys, matchs)
- Q4: correctly resolved "~~two~~ three" to **"three"** (dropped the
  struck-through word, kept the correction), rest verbatim including
  misspellings (parliment, contry, distrct, chek, togther, seperation)

**Result: exact match against `sample2.expected.md`**, including both
tricky cases (strike-through vs. circled-selection, and inline word
correction).

## Caveat — still not a real accuracy result

Both samples are computer-rendered handwriting fonts. They now also
exercise strike-throughs, corrections, rotation, and misspellings, which
is a meaningfully harder test than sample1 alone — but real handwriting
(actual pen/pencil strokes, inconsistent letter formation, real paper
noise, phone-camera lighting/skew) remains untested. Treat this as
"pipeline handles the known hard *shapes* of exam markup correctly",
not as "ready for real papers".

## Next
- Get 2-3 real handwritten samples when available (your own handwriting
  is fine, anonymized) and re-run this same check for a real accuracy
  number before starting Step 1 (grading logic). Until then, synthetic
  samples can keep covering more edge cases (e.g. double-marked MCQ,
  very faint/small handwriting, multi-line answer with no clear
  structure).
