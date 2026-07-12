import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.csv")
OUTPUT_FILE = Path(__file__).with_name("student_summary.csv")


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_FILE)


def analyze_data(df: pd.DataFrame):
    average_scores = (
        df.groupby("Course", as_index=False)["Score"]
        .mean()
        .round(2)
        .sort_values("Score", ascending=False)
    )

    top_student = df.loc[df["Score"].idxmax()]
    return average_scores, top_student


def main() -> None:
    df = load_data()

    print("Student records:")
    print(df)

    average_scores, top_student = analyze_data(df)

    print("\nAverage score by course:")
    print(average_scores)

    print("\nTop performer:")
    print(top_student.to_string())

    average_scores.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSaved summary to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
