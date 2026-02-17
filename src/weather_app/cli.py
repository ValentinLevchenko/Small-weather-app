import argparse
from weather_app.analysis import analyse_weather, check_dataset


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="weather-cli", description="Weather analysis CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    summary = subparsers.add_parser("summary", help="Compute summary metrics")
    summary.add_argument("--input", required=True, help="Path to weather CSV")
    summary.add_argument("--start", required=False, help="Start date YYYY-MM-DD")
    summary.add_argument("--end", required=False, help="End date YYYY-MM-DD")

    check = subparsers.add_parser("check-data", help="Validate input dataset")
    check.add_argument("--input", required=True, help="Path to weather CSV")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "summary":
        result = analyse_weather(args.input, start=args.start, end=args.end)
        print(result)
    elif args.command == "check-data":
        report = check_dataset(args.input)
        print(report)


if __name__ == "__main__":
    main()