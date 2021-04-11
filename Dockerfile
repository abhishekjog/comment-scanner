FROM python:3.8.2-slim-buster

WORKDIR /app
COPY main.py main.py

ENTRYPOINT ["python", "/app/main.py"]
