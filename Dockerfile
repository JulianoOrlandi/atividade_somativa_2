FROM ubuntu:latest

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN apt-get update

RUN apt-get remove --purge -y python3.7

RUN apt-get install -y python3.6 \
    && ln -s /usr/bin/python3.6 /usr/bin/python3

RUN apt-get -y install python3-pip

RUN apt-get -y install python3-flask

RUN apt-get -y install python3-requests

CMD python app.py

CMD ["tail", "-f", "/dev/null"]