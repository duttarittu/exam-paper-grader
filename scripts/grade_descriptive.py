"""
Step 2: descriptive-question grading with partial credit, against an
explicit rubric (docs/rubrics/social_studies_timezones.md).

How this differs from MCQ grading (scripts/grade_mcq.py):
- There's no single right/wrong answer to compare against. Instead, the
  rubric breaks the question into criteria with their own max points.
- Per-criterion scores and justifications below were assigned by reading
  each student answer against the rubric (this is the one place in the
  pipeline where judgment is required) - but the TOTAL is still always
  recomputed here in code by summing the per-criterion points, never
  taken as a single self-reported number. Full marks are only possible
  if every criterion is fully met; no criterion may award more than its
  own max_points (enforced below, not just assumed).

Run: python3 scripts/grade_descriptive.py
"""

RUBRIC = {
    "question": "Why do we have different time zones?",
    "max_marks": 6,
    "criteria": [
        {
            "id": "C1",
            "description": "Mentions the Earth rotates/spins on its own axis",
            "max_points": 2,
        },
        {
            "id": "C2",
            "description": "Explains rotation causes day on one side, night on the opposite side, at the same time",
            "max_points": 2,
        },
        {
            "id": "C3",
            "description": "Connects this to why countries set different clock times (matching the sun's position)",
            "max_points": 2,
        },
    ],
}

# Each entry: the transcribed student answer, and per-criterion points +
# justification assigned by reading the answer against the rubric above.
STUDENT_ANSWERS = {
    "Rohan - strong answer (reused from sample2.jpg Q3)": {
        "text": (
            "becuase the earth is round and it spin on its own axis so wen one "
            "side facs the sun it is day there and the oposite side is nite. so "
            "contrys on diff side of the globe keep diff time so that there "
            "clock matchs with wen the sun is up for them"
        ),
        "scores": [
            {"id": "C1", "points": 2, "why": "explicitly says 'it spin on its own axis'"},
            {"id": "C2", "points": 2, "why": "explicitly describes one side facing the sun (day) and the opposite side (night)"},
            {"id": "C3", "points": 2, "why": "explicitly links differing clocks to the sun being up in that region"},
        ],
    },
    "Priya - weak/partial answer": {
        "text": (
            "Because the earth is big and round, some parts are far from each "
            "other so time is different in different places."
        ),
        "scores": [
            {"id": "C1", "points": 1, "why": "mentions the Earth is round but never mentions rotation/spinning - partial credit per rubric"},
            {"id": "C2", "points": 0, "why": "no day/night mechanism explained at all"},
            {"id": "C3", "points": 1, "why": "says time differs by place, but never explains why (no link to sun/rotation) - partial credit per rubric"},
        ],
    },
}


def grade(rubric, scores):
    """Sums per-criterion points in code (never trusts a reported total).

    Also enforces that no criterion's awarded points exceed its own
    max_points, so a bad judgment call can't silently overshoot.
    """
    criteria_by_id = {c["id"]: c for c in rubric["criteria"]}
    results = []
    total_awarded = 0

    for score in scores:
        criterion = criteria_by_id[score["id"]]
        awarded = score["points"]
        if awarded > criterion["max_points"]:
            raise ValueError(
                f"{score['id']} awarded {awarded} but max is {criterion['max_points']}"
            )
        results.append({
            "id": score["id"],
            "description": criterion["description"],
            "awarded": awarded,
            "max_points": criterion["max_points"],
            "why": score["why"],
        })
        total_awarded += awarded

    return results, total_awarded


def print_report(student_label, answer_text, rubric, results, total_awarded):
    print("=" * 70)
    print(student_label)
    print(f"Question: {rubric['question']}")
    print(f"Answer: {answer_text}")
    print("-" * 70)
    for r in results:
        print(f"[{r['id']}] {r['description']}")
        print(f"      awarded: {r['awarded']}/{r['max_points']}  -  {r['why']}")
    print("-" * 70)
    print(f"TOTAL: {total_awarded}/{rubric['max_marks']}")


if __name__ == "__main__":
    for student_label, answer in STUDENT_ANSWERS.items():
        results, total_awarded = grade(RUBRIC, answer["scores"])
        print_report(student_label, answer["text"], RUBRIC, results, total_awarded)
        print()
