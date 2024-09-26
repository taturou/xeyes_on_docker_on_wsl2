FROM python:3

RUN apt-get update
RUN apt install -y x11-apps

WORKDIR /usr/src

