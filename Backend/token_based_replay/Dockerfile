# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY token_based_replay.py /app

VOLUME ["/token_based_replay"]

ENTRYPOINT [ "python3", "token_based_replay.py"]