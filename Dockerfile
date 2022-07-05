FROM python:3.8-slim

RUN apt-get update && apt-get install -y git

COPY . /leech
RUN apt update
RUN pip install --upgrade pip
RUN apt-get install gcc -y
RUN apt-get install postgresql-client -y
RUN apt-get install libpq-dev -y
RUN apt-get install vim -y

RUN apt-get install -y wget unzip
RUN apt-get install -y gnupg2

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

RUN pip install -r /leech/requirements.txt
RUN pip install -r /leech/requirements.lint.txt
RUN pip install -r /leech/requirements.test.txt

ENV PYTHONPATH .
ENV PYTHONDONTWRITEBYTECODE 1

RUN python --version

WORKDIR /leech
