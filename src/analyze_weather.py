import pandas as pd

def analyse_weather(path):

    weather = pd.read_csv(path)

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


path = "data/weather_hourly.csv"
analyse_weather(path)