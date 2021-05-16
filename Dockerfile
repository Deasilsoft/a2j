FROM python:alpine
RUN apk --no-cache upgrade \
 && apk --no-cache update \
 && apk --no-cache add build-base

# SET ENVIRONMENT VARIABLES
ENV HOME=/home/a2j

# SETUP WORK DIRECTORY
WORKDIR ${HOME}
ADD . $HOME

# INSTALL PYTHON REQUIREMENTS
RUN pip install -r requirements.txt

# EXPOSE PORT
EXPOSE 8080

# RUN SERVER
CMD python app.py
