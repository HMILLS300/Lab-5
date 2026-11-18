FROM python:3.9-slim

WORKDIR /app

RUN pip install Flask gunicorn

COPY . .

CMD ["python3", "app.py"]

