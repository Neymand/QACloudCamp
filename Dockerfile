FROM python:3.9.17-slim-bullseye
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get install -y git python3 python3-venv

RUN mkdir -p /opt/jsonplaceholder
WORKDIR /opt/jsonplaceholder

RUN cd /opt/jsonplaceholder
COPY jsonplaceholder_tests.py /opt/jsonplaceholder
COPY requirements.txt /opt/jsonplaceholder
COPY start.sh /opt/jsonplaceholder

RUN python3 -m venv virtualenv
RUN source virtualenv/bin/activate
RUN pip3 install --upgrade pip; pip3 install -r requirements.txt

ENTRYPOINT /opt/jsonplaceholder/start.sh
