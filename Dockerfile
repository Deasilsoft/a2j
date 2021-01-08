FROM python:alpine

RUN apk update \
 && apk upgrade \
 && apk add build-base

# SET HOME ENVIRONMENT
ENV HOME=/home/a2j
WORKDIR ${HOME}
ADD . $HOME

# INSTALL REQUIREMENTS
RUN pip install -r requirements.txt

# RUN SERVER
RUN python app.py

# EXPOSE PORT 4000
EXPOSE 4000
