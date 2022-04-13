# Dockerfile

# pull the official docker image
FROM python:3.9.4
MAINTAINER VIKTOR NIKOLAEV

# set work directory
WORKDIR /counter_of_statistics

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .