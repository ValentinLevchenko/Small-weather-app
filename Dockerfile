FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir dash dash-bootstrap-components pandas plotly numpy scipy matplotlib

COPY src/ ./src/
COPY data/ ./data/

CMD ["python", "src/weather_app/dash_app.py"]

#CMD ["python","src/analyze_weather.py", "--input","data/weather_hourly.csv","--min-temp","0"]



"""
----
FROM python:3.14-trixie

COPY weather*.whl /tmp
RUN ls -l /tmp/weather*.whl
RUN pip install /tmp/weather*.whl
"""