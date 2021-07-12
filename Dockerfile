FROM python:alpine

# INSTALL BUILD-BASE
RUN ["apk", "--no-cache", "add", "build-base"]

# SET ENVIRONMENT VARIABLES
ENV HOME=/home/a2j

# SETUP WORK DIRECTORY
WORKDIR ${HOME}
COPY . .

# INSTALL PYTHON REQUIREMENTS
RUN ["pip", "install", "-r", "requirements.txt"]

# RUN APP ON PORT 8080
EXPOSE 8080
CMD ["python", "src/main.py"]
