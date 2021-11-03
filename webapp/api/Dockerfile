FROM python:3.8
LABEL maintainer="nasak"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /api
WORKDIR /api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
