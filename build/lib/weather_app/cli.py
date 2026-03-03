import argparse
import pandas as pd
from weather_app.analysis import analyse_weather, check_dataset, plot_temperature_trend


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="weather-cli", description="Weather analysis CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    summary = subparsers.add_parser("summary", help="Compute summary metrics")
    summary.add_argument("--input", required=True, help="Path to weather CSV")
    summary.add_argument("--start", required=False, help="Start date YYYY-MM-DD")
    summary.add_argument("--end", required=False, help="End date YYYY-MM-DD")

    check = subparsers.add_parser("check-data", help="Validate input dataset")
    check.add_argument("--input", required=True, help="Path to weather CSV")

    plot = subparsers.add_parser("plot", help="Plot temperature trend")
    plot.add_argument("--input", required=True, help="Path to weather CSV")
    plot.add_argument("--output", default = "results/temperature_2m_trend.png", help="Path to store the plot")

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
    elif args.command == "plot":
        df = pd.read_csv(args.input)
        plot_temperature_trend(df, out_path=args.output)
        print(f"Plot saved to {args.output}")


if __name__ == "__main__":
    main()