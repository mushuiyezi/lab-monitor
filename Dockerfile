FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY monitor.py ./
RUN mkdir -p /app/logs

VOLUME ["/app/logs"]

CMD ["python", "monitor.py"]
