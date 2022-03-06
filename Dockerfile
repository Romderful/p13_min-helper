FROM python:3.10.1-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN pip install --upgrade pip

COPY . /app/

RUN pip install -r backend/requirements.txt
RUN python backend/manage.py collectstatic --noinput
