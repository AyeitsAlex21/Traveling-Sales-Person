FROM python:3.8
LABEL maintainer="nasak"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /web
WORKDIR /web
RUN pip install -r requirements.txt
