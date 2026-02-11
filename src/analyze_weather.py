import pandas as pd
import argparse

def analyse_weather(path, start=None, end=None, min_temp=None):

    weather = pd.read_csv(path)

    weather["time"] = pd.to_datetime(weather["time"], unit="ms")
    print(weather["time"].head())


    if start is not None:
        time_start = pd.to_datetime(start)
        print(time_start)

        weather = weather[weather["time"] >= time_start] 

    if end is not None:
        time_end = pd.to_datetime(end)
        weather = weather[weather["time"]< time_end] 
        
    if min_temp is not None:
        weather = weather[weather["temperature_2m"]>=min_temp]

    

    temp_min = weather["temperature_2m"].min()
    temp_max = weather["temperature_2m"].max()
    temp_avg = weather["temperature_2m"].mean()

    humi_avg = weather["relative_humidity_2m"].mean()
    
    wind_max = weather["wind_speed_10m"].max()

    print("The temperature values:\n")
    print(f"min: {temp_min:.3f}")
    print(f"max: {temp_max:.3f}")
    print(f"avg: {temp_avg:.3f}")

    print(f"The mean relative humidity at 2 meters above ground: {humi_avg:.3f}")
    print(f"The maximum wind speed at 10 meters above ground: {wind_max:.3f}")


def main():
    parser = argparse.ArgumentParser(description="Weather analysis script")

    parser.add_argument("--input", required=True, help = "Path to input CSV file")

    parser.add_argument("--start", help="Start date")
    parser.add_argument("--end", help="End date")
    parser.add_argument("--min-temp", help="Minimum temperature filter")

    args = parser.parse_args()

    if not(args.start or args.end or args.min_temp):
        parser.error("You must provide at least one filter among the following options : --start, --end, --min-temp")

    analyse_weather(args.input, args.start, args.end, args.min_temp)

if __name__=='__main__':
    main()