FROM python:alpine
RUN apk update \
 && apk upgrade \
 && apk add build-base

# SET ENVIRONMENT VARIABLES
ENV HOME=/home/a2j

# SETUP WORK DIRECTORY
WORKDIR ${HOME}
ADD . $HOME

# INSTALL PYTHON REQUIREMENTS; CACHE IT
RUN pip install -r requirements.txt

# EXPOSE PORT
EXPOSE 8080

# RUN SERVER
CMD python app.py
