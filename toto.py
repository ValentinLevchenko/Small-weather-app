import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html


df = pd.read_csv("data/weather_hourly.csv")
df["time"] = pd.to_datetime(df["time"], unit="ms", errors="coerce")
df = df.dropna(subset=["time"]).sort_values("time")

app = Dash(__name__)
server = app.server

fig = px.line(df.head(300), x="time", y="temperature_2m", title="Temperature (first 300 rows)")

app.layout = html.Div(
    [
        html.H1("Weather Dashboard"),
        dcc.Graph(figure=fig),
    ]
)

if __name__ == "__main__":
    app.run(debug=True, port=8050)