FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas matplotlib

COPY src/ ./src/
COPY data/ ./data/

CMD ["python","src/analyze_weather.py", "--input","data/weather_hourly.csv","--min-temp","0"]