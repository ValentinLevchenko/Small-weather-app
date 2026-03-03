import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

METRICS = {
    "temperature_2m": "Temperature (deg C)",
    "relative_humidity_2m": "Relative Humidity (%)",
    "wind_speed_10m": "Wind Speed (km/h)",
    "surface_pressure": "Surface Pressure (hPa)",
}

df = pd.read_csv("../../data/weather_hourly.csv")
df["time"] = pd.to_datetime(df["time"], unit="ms", errors="coerce")
df = df.dropna(subset=["time"]).sort_values("time")

app = Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.H1("Weather Dashboard"),
        dcc.DatePickerRange(
            id="date-range",
            start_date=df["time"].min().date(),
            end_date=df["time"].max().date(),
            display_format="YYYY-MM-DD",
        ),
        dcc.Dropdown(
            id="metric",
            options=[{"label": label, "value": key} for key, label in METRICS.items()],
            value="temperature_2m",
            clearable=False,
            style={"width": "420px", "marginTop": "12px"},
        ),
        html.Div(id="stats", style={"marginTop": "16px"}),
        dcc.Graph(id="weather-graph"),
    ],
    style={"maxWidth": "1100px", "margin": "0 auto", "padding": "16px"},
)


@app.callback(
    Output("weather-graph", "figure"),
    Output("stats", "children"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
    Input("metric", "value"),
)
def update_dashboard(start_date, end_date, metric):
    filtered = df[(df["time"] >= start_date) & (df["time"] <= end_date)]
    filtered = filtered.dropna(subset=[metric])

    if filtered.empty:
        return px.line(title="No data for selected filters"), html.Div("No rows in selected range.")

    fig = px.line(filtered, x="time", y=metric, title=f"{METRICS[metric]} over time")
    stats = html.Ul(
        [
            html.Li(f"Rows: {len(filtered)}"),
            html.Li(f"Mean: {filtered[metric].mean():.2f}"),
            html.Li(f"Min: {filtered[metric].min():.2f}"),
            html.Li(f"Max: {filtered[metric].max():.2f}"),
        ]
    )
    return fig, stats


if __name__ == "__main__":
    app.run(debug=True, port=8050)