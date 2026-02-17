import argparse
from weather_app.analysis import analyse_weather, check_dataset, plot_temperature_trend


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="weather-cli", description="Weather analysis CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    summary = subparsers.add_parser("summary", help="Compute summary metrics")
    summary.add_argument("--input", required=True, help="Path to weather CSV")
    summary.add_argument("--start", required=False, help="Start date DD_MM_YYYY")
    summary.add_argument("--end", required=False, help="End date DD_MM_YYYY")
    summary.add_argument("--min_temp", required=False, help="Minimum temperature required")

    check = subparsers.add_parser("check-data", help="Validate input dataset")
    check.add_argument("--input", required=True, help="Path to weather CSV")

    plot = subparsers.add_parser("plot", help="Plot the data")
    plot.add_argument("--input", required=True, help="Path to weather CSV")
    plot.add_argument("--start", required=False, help="Start date DD_MM_YYYY")
    plot.add_argument("--end", required=False, help="End date DD_MM_YYYY")
    plot.add_argument("--min_temp", required=False, help="Minimum temperature required")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "summary":
        analyse_weather(args.input, start=args.start, end=args.end, min_temp=args.min_temp)
    elif args.command == "check-data":
        check_dataset(args.input)
    elif args.command == "plot":
        weather = analyse_weather(args.input, start=args.start, end=args.end, min_temp=args.min_temp)
        plot_temperature_trend(weather)


if __name__ == "__main__":
    main()