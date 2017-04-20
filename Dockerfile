FROM python:3.6-alpine
MAINTAINER Vladimir S. <vladimir.s@gowombat.team>
RUN apk add --no-cache g++ make python3-dev jpeg-dev zlib-dev libffi-dev postgresql-dev musl-dev

COPY . /application
WORKDIR /application

RUN pip3 install -r requirements.txt
