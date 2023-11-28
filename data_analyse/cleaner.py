import os
import csv

PATH = os.path.join(os.pardir, "linkedin/output.csv")


def clean() -> list[str]:
    if not os.path.exists(PATH):
        raise ValueError(
            "Path is incorrect. Please, run spider before analysing"
        )
    with open(PATH, "r") as f:
        csv_reader = csv.DictReader(f)
        return [row["text"].lower() for row in csv_reader]
