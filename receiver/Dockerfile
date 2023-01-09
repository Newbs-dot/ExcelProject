FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /receiver
WORKDIR /receiver

COPY ./requirements.txt /receiver/
RUN pip install -r requirements.txt

COPY ./ /receiver