[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1RHvwtZb)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22606584)

# Reproducible Mini Weather Analysis

**Goal:** Build a small reproducible weather analysis workflow from an hourly CSV dataset and document how to run it locally and with Docker.

## Data description

| **Column** | **Description** | **Unit** |
| :--- | :--- | :--- |
| **cloud_cover** | Total cloud cover as a percentage of the sky. (0 = clear sky, 100 = fully overcast) | % |
| **diffuse_radiation** | Solar radiation reaching the ground that has been scattered by the atmosphere. | W/m² |
| **direct_radiation** | Solar radiation reaching the ground directly from the sun. | W/m² |
| **relative_humidity_2m** | Relative humidity at 2 meters above the ground. | % |
| **surface_pressure** | Atmospheric pressure at the surface. | hPa |
| **temperature_2m** | Air temperature measured at 2 meters above the ground. | deg C |
| **time** | Date and time of the observation in Unix timestamp format. | Milliseconds (ms) |
| **wind_direction_10m** | Wind direction measured at 10 meters above the ground. (0/360 = North, 90 = East, 180 = South, 270 = West ) | deg |
| **wind_speed_10m** | Wind speed measured at 10 meters above the ground. | km/h |

## Instructions for running
At the base of the project execute : 
```
python src/analyze_weather.py --input data/weather_hourly.csv --start 2023-01-01
```
With:
* --input: the link to the csv file that we want to read (mandatory !)
options: (At least one)
* --start: starting date from where we want to run the calculation
* --end: ending date from where we want to stop the calculation
* --min-temp : minumium temperature required to be part of the calculation

Please note that in the file weather_hourly.csv the date stop around the end of 2023.