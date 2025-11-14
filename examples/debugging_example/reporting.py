from typing import Dict, List, Tuple, Optional

from config import DAILY_STEP_GOAL
from analysis import summarize_week


def generate_weekly_report(grouped_records: Dict[Tuple[int, int], List[Dict]]) -> str:
    """
    Generate a multi-line string summarizing all weeks in the dataset.
    """
    lines: List[str] = []

    for (year, week), recs in sorted(grouped_records.items()):
        summary: Optional[Dict] = summarize_week(recs)
        if summary is None:
            continue

        header = f"Week {week} of {year}"
        lines.append(header)
        lines.append("-" * len(header))
        lines.append(f"Days recorded:            {summary['days']}")
        lines.append(f"Average steps:            {summary['avg_steps']:.0f}")
        lines.append(f"Inactive days (0 steps):  {summary['inactive_days']}")
        lines.append(
            f"Days below goal ({DAILY_STEP_GOAL}): {summary['below_goal_days']}"
        )
        lines.append("")  # blank line between weeks

    return "\n".join(lines)
