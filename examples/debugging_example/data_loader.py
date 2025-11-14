import csv
from typing import List, Dict, Optional


def load_raw_data(csv_path: str) -> List[Dict[str, Optional[str]]]:
    """
    Load daily step counts from a CSV file.

    Each row in the CSV should have:
        - date: ISO date string (YYYY-MM-DD)
        - steps: step count as a string (may be invalid or empty)
    """
    records: List[Dict[str, Optional[str]]] = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Normalize missing values to None
            date = row.get("date") or None
            steps = row.get("steps") or None

            records.append({"date": date, "steps": steps})

    return records
