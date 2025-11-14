from collections import defaultdict
from typing import Dict, List, Tuple, Optional

from config import DAILY_STEP_GOAL


def group_by_week(records: List[Dict]) -> Dict[Tuple[int, int], List[Dict]]:
    """
    Group records by ISO year-week.

    Returns a dict mapping (year, week) -> list of records.
    """
    grouped: Dict[Tuple[int, int], List[Dict]] = defaultdict(list)

    for rec in records:
        year, week, _ = rec["date"].isocalendar()
        grouped[(year, week)].append(rec)

    return grouped


def categorize_activity(steps: int) -> str:
    """Categorize daily activity level based on steps."""
    if steps == 0:
        return "inactive"
    if steps < 5000:
        return "low"
    if steps < DAILY_STEP_GOAL:
        return "medium"
    if steps < 12000:
        return "active"
    return "very active"


def summarize_week(records: List[Dict]) -> Optional[Dict]:
    """
    Compute weekly summary statistics.

    Returns a dict with:
        - "days": number of days in the week
        - "avg_steps": average steps per day
        - "inactive_days": number of days with 0 steps
        - "below_goal_days": days below DAILY_STEP_GOAL
    """
    if not records:
        return None

    total_steps = 0
    inactive_days = 0
    below_goal_days = 0

    for rec in records:
        steps = rec["steps"]
        total_steps += steps

        category = categorize_activity(steps)
        if category == "inactive":
            inactive_days += 1

        if steps < DAILY_STEP_GOAL:
            below_goal_days += 1

    avg_steps = total_steps / len(records)

    return {
        "days": len(records),
        "avg_steps": avg_steps,
        "inactive_days": inactive_days,
        "below_goal_days": below_goal_days,
    }
