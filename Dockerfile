FROM python:slim
RUN apt-get update \
 && apt-get upgrade -y

# SET ENVIRONMENT VARIABLES
ENV HOME=/home/a2j
ENV DEBUG=TRUE

# SETUP WORK DIRECTORY
WORKDIR ${HOME}
ADD . $HOME

# INSTALL PYTHON REQUIREMENTS; CACHE IT
RUN pip install -r requirements.txt

# EXPOSE PORT
EXPOSE 8080

# RUN SERVER
CMD python app.py
