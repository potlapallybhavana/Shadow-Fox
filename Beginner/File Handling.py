"""
Beginner Task 7: File Handling
- Read student_marks.csv
- Create dict per student, add total_marks and average
- Write to a new CSV: student_marks_with_totals.csv
Expected columns include: name or id + subject marks.
"""
import csv
from pathlib import Path

def process_marks(input_csv: str, output_csv: str):
    input_path = Path(input_csv)
    if not input_path.exists():
        raise FileNotFoundError(f"{input_csv} not found. Place it in this folder.")

    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Infer which columns are numeric marks (exclude non-numeric fields like 'Name', etc.)
    def to_float(x):
        try:
            return float(x)
        except Exception:
            return None

    numeric_cols = [c for c in reader.fieldnames if all(to_float(r.get(c)) is not None for r in rows)]
    processed = []
    for r in rows:
        marks = [float(r[c]) for c in numeric_cols]
        total = sum(marks)
        avg = total / len(marks) if marks else 0.0
        out = dict(r)
        out["total_marks"] = f"{total:.2f}"
        out["average"] = f"{avg:.2f}"
        processed.append(out)

    out_fields = reader.fieldnames + ["total_marks", "average"]
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(processed)
    return output_csv

if __name__ == "__main__":
    try:
        out = process_marks("student_marks.csv", "student_marks_with_totals.csv")
        print("Wrote:", out)
    except FileNotFoundError as e:
        print(e)
        print("Download the dataset from Kaggle and save as 'student_marks.csv' in this folder.")
