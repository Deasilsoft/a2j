FROM python:alpine

RUN apk update \
 && apk upgrade \
 && apk add build-base

ENV HOME=/home/a2j

WORKDIR ${HOME}
ADD . $HOME

RUN ["pip", "install", "mgz"]
