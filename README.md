[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1RHvwtZb)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22606584)

# Reproducible Mini Weather Analysis

**Goal:** Build a small reproducible weather analysis workflow from an hourly CSV dataset and document how to run it locally and with Docker.



## Instructions for running
For the project root, execute: 
```
python src/analyze_weather.py --input data/weather_hourly.csv --start 2023-01-01
```

With:
* `--input`: the path to the CSV file to be analyzed (`data/weather_hourly.csv` is used by default)

Options:
* `--start`: starting date from which the calculation begins
* `--end`: ending date at which the calculation stops
* `--min-temp` : minumum temperature required to be included in the calculation

Please note that data in `data/weather_hourly.csv` covers approximately the period between 1st January 2023 and 31st December 2023.

## Dockerfile

We created a Dockerfile to produce a stable and reproductible execution environment.

We used the official image `python:3.11-slim` as the base. This light version allows to reduce the size of the final image. 

We then defined the working directory and copied `src` and `data` folders into the container. 

The required library (`pandas`) is installed, and the default `CMD` is set to enable automatic execution of the analysis script whenever the container starts.


