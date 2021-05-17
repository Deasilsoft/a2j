FROM python:alpine

# INSTALL BUILD-BASE
RUN ["apk", "--no-cache", "add", "build-base"]

# INSTALL VIRTUAL ENVIRONMENT
RUN ["pip", "install", "virtualenv"]

# SET ENVIRONMENT VARIABLES
ENV HOME=/home/a2j
ENV VENV=venv

# SETUP WORK DIRECTORY
WORKDIR ${HOME}
COPY . .

# SETUP VIRTUAL ENVIRONMENT
RUN ["virtualenv", "${VENV}"]
RUN ["${VENV}/bin/pip", "install", "-r", "requirements.txt"]

# RUN APP ON PORT 8080
EXPOSE 8080
CMD ["${VENV}/bin/python", "app.py"]
