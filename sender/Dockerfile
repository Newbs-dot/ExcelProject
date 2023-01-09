FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /sender
WORKDIR /sender

COPY ./requirements.txt /sender/
RUN pip install -r requirements.txt

COPY ./ /sender