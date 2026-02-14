import pandas as pd
import argparse

def analyse_weather(path, start=None, end=None, min_temp=None):

    weather = pd.read_csv(path)

    weather["time"] = pd.to_numeric(weather["time"], errors = "coerce")
    weather["time"] = pd.to_datetime(weather["time"], unit = "ms", errors = "coerce")
    weather = weather.dropna(subset = ["time"])

 #   print(weather["time"].head())


    if start is not None:
        time_start = pd.to_datetime(start)
 #       print(time_start)

        weather = weather[weather["time"] >= time_start] 

    if end is not None:
        time_end = pd.to_datetime(end)
        weather = weather[weather["time"] < time_end] 
        
    if min_temp is not None:
        weather = weather[weather["temperature_2m"] >= min_temp]

    temp_min = weather["temperature_2m"].min()
    temp_max = weather["temperature_2m"].max()
    temp_avg = weather["temperature_2m"].mean()

    humi_avg = weather["relative_humidity_2m"].mean()
    
    wind_max = weather["wind_speed_10m"].max()

    print("\nThe temperature values:")
    print("  min  |  max   |  avg  ")
    print(f"{temp_min:.3f} | {temp_max:.3f} | {temp_avg:.3f}")

    print(f"Mean relative humidity at 2 meters above ground: {humi_avg:.3f}")
    print(f"Maximum wind speed at 10 meters above ground: {wind_max:.3f}\n")


def main():
    parser = argparse.ArgumentParser(description="Weather analysis script")

    parser.add_argument("--input", required=True, help = "Path to input CSV file")

    parser.add_argument("--start", help="Start date")
    parser.add_argument("--end", help="End date")
    parser.add_argument("--min-temp", type = float , help="Minimum temperature filter")

    args = parser.parse_args()

    if args.start is None and args.end is None and args.min_temp is None:
        parser.error("You must provide at least one filter among the following options : --start, --end, --min-temp")

    analyse_weather(args.input, args.start, args.end, args.min_temp)

if __name__=='__main__':
    main()