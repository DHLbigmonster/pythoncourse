import datetime
from typing import List, Dict, Optional


def parse_date(date_str: str) -> datetime.date:
    """Convert an ISO date string (YYYY-MM-DD) to a datetime.date object."""
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()


def parse_steps(steps_str: Optional[str]) -> Optional[int]:
    """Convert the steps value to an integer if possible, otherwise return None."""
    if steps_str is None:
        return None

    try:
        return int(steps_str)
    except (TypeError, ValueError):
        return None


def parse_record(record: Dict[str, Optional[str]]) -> Optional[Dict]:
    """
    Parse a raw record into a normalized dict, or return None if invalid.

    Normalized record:
        - "date": datetime.date
        - "steps": int
    """
    date_str = record.get("date")
    steps_str = record.get("steps")

    if not date_str:
        return None

    try:
        date = parse_date(date_str)
    except ValueError:
        return None

    steps = parse_steps(steps_str)
    if steps is None:
        return None

    return {"date": date, "steps": steps}


def clean_data(raw_records: List[Dict[str, Optional[str]]]) -> List[Dict]:
    """
    Parse and filter the raw data.

    Returns a list of valid records with parsed dates and integer step counts.
    """
    cleaned: List[Dict] = []

    for record in raw_records:
        parsed = parse_record(record)
        if parsed and parsed["steps"]:
            cleaned.append(parsed)

    return cleaned
