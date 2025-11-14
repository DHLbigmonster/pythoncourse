from data_loader import load_raw_data
from cleaning import clean_data
from analysis import group_by_week
from reporting import generate_weekly_report


def main():
    csv_path = "data/steps.csv"

    raw = load_raw_data(csv_path)
    cleaned = clean_data(raw)
    weekly = group_by_week(cleaned)

    report = generate_weekly_report(weekly)
    print(report)


if __name__ == "__main__":
    main()
