FROM python:3.6-alpine
MAINTAINER Vladimir S. <vladimir.s@gowombat.team>
RUN apk add --no-cache g++ make python3-dev jpeg-dev zlib-dev libffi-dev postgresql-dev musl-dev

COPY . /application
RUN chmod +x /application/docker-entrypoint.sh
WORKDIR /application

RUN pip install -r requirements.txt
