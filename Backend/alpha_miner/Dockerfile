# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /alpha_miner

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY alpha_miner.py .
COPY running-example.xes .

CMD [ "python3", "alpha_miner.py"]