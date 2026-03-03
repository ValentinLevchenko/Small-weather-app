FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    pandas \
    matplotlib \
    plotly \
    numpy \
    scipy \
    dash

COPY src/ ./src/
COPY data/ ./data/

ENV PYTHONPATH=/app/src

EXPOSE 8050

CMD ["python","src/weather_app/dash_app.py"]