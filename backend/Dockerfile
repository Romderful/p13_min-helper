FROM python:3.9.6
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY backend/requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
