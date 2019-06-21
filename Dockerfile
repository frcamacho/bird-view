FROM ubuntu:18.10

RUN apt-get update -y
RUN apt-get install -y python3 python3-dev python3-pip nginx

RUN pip3 install uwsgi

COPY . /bird-view
WORKDIR /bird-view

RUN pip3 install -r requirements.txt

CMD gunicorn -b 0.0.0.0:5000 run
