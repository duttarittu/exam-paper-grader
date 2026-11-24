"""
Step 1: MCQ grading, single paper, single subject, hardcoded answer key.

Deliberately simple and hardcoded for now:
- ANSWER_KEY and STUDENT_ANSWERS are hardcoded Python dicts (not read from
  a file yet) representing the teacher's answer key and the options
  transcribed from a student's paper.
- Marks are computed here in plain code, never by an LLM, per this
  project's standing rule: the model may help *transcribe* what a student
  circled, but never self-reports a total.
- Output goes to the console only. Excel output comes in Step 4.

Run: python3 scripts/grade_mcq.py
"""

STUDENT_NAME = "Rohan Mehta"
ROLL_NO = "12"
SUBJECT = "Mathematics"

# question_id -> (correct_option, marks_for_this_question)
ANSWER_KEY = {
    "Q1": ("b", 2),
    "Q2": ("b", 2),
    "Q3": ("c", 2),
    "Q4": ("a", 2),
    "Q5": ("d", 2),
}

# question_id -> option the student circled.
# For now this is typed in by hand after reading samples/sample3_mcq.jpg;
# later steps will fill this in from the vision/transcription step instead.
STUDENT_ANSWERS = {
    "Q1": "b",
    "Q2": "b",
    "Q3": "c",
    "Q4": "a",
    "Q5": "c",  # selected 3.16, correct answer is 3.14 (d) -> wrong
}


def grade(answer_key, student_answers):
    """Returns a list of per-question results and the recomputed total.

    Each result is a dict: question_id, selected, correct, is_correct,
    marks_awarded, max_marks. The total is summed here in code, never
    taken from any single upstream value.
    """
    results = []
    total_awarded = 0
    total_possible = 0

    for question_id, (correct_option, max_marks) in answer_key.items():
        selected = student_answers.get(question_id)
        is_correct = selected is not None and selected == correct_option
        marks_awarded = max_marks if is_correct else 0

        results.append({
            "question_id": question_id,
            "selected": selected,
            "correct": correct_option,
            "is_correct": is_correct,
            "marks_awarded": marks_awarded,
            "max_marks": max_marks,
        })

        total_awarded += marks_awarded
        total_possible += max_marks

    return results, total_awarded, total_possible


def print_report(name, roll_no, subject, results, total_awarded, total_possible):
    print(f"Student: {name}  (Roll No: {roll_no})")
    print(f"Subject: {subject}")
    print("-" * 50)
    for r in results:
        status = "CORRECT" if r["is_correct"] else "WRONG"
        selected = r["selected"] if r["selected"] is not None else "(no answer)"
        print(
            f"{r['question_id']}: selected={selected}  correct={r['correct']}  "
            f"[{status}]  marks={r['marks_awarded']}/{r['max_marks']}"
        )
    print("-" * 50)
    print(f"TOTAL: {total_awarded}/{total_possible}")


if __name__ == "__main__":
    results, total_awarded, total_possible = grade(ANSWER_KEY, STUDENT_ANSWERS)
    print_report(STUDENT_NAME, ROLL_NO, SUBJECT, results, total_awarded, total_possible)
