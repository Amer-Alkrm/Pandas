FROM python:3.9.6-slim-buster AS base

FROM base AS build

RUN apt-get update \
    && apt-get install libpq-dev gcc git make -y
RUN apt install python3-dev build-essential -y

RUN apt install libssl-dev -y 
RUN apt install default-libmysqlclient-dev -y

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENV PYTHONPATH=/app/
