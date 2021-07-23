FROM python:3.8-slim

RUN apt-get update 

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 8080

CMD uvicorn main:app --port 8080 --host 0.0.0.0