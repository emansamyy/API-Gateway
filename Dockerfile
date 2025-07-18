FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/bookstore_gateway

WORKDIR /app

RUN apt-get update && apt-get install -y gcc netcat-openbsd && apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "bookstore_gateway.wsgi:application", "--bind", "0.0.0.0:8000"]
