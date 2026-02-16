[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1RHvwtZb)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22606584)

# Reproducible Mini Weather Analysis

**Goal:** Build a small reproducible weather analysis workflow from an hourly CSV dataset and document how to run it locally and with Docker.



## Instructions for running
At the base of the project execute : 
```
python src/analyze_weather.py --input data/weather_hourly.csv --start 2023-01-01
```

With:
* --input: the path to the CSV file that we want to read

Options:
* --start: starting date from where we want to run the calculation
* --end: ending date from where we want to stop the calculation
* --min-temp : minumum temperature required to be part of the calculation

Please note that in the file weather_hourly.csv the date stop around the end of 2023.

## Dockerfile

We created a Dockerfile to produice a stable and reproductible execution environment.

We used the official image "python:3.11-slim" has a base.

This lite version allow to reduce the size of the final image. 

Then we defined the main folder containing the code. 

Then the "src" and "data folders were copied in the conteneur. 

To execute everything, we had to install the library "pandas" as well as the "CMD" for the automation of the execution of the script every time we start the container.


