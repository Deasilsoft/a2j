FROM python:alpine

# SET ENVIRONMENT VARIABLES
ENV HOME=/home/a2j

# SET WORK DIRECTORY
WORKDIR ${HOME}

# INSTALL PREREQUISITES TO PYTHON DEPENDENCIES
RUN ["apk", "--no-cache", "add", "build-base"]
RUN ["apk", "--no-cache", "add", "tiff-dev"]
RUN ["apk", "--no-cache", "add", "jpeg-dev"]
RUN ["apk", "--no-cache", "add", "openjpeg-dev"]
RUN ["apk", "--no-cache", "add", "zlib-dev"]
RUN ["apk", "--no-cache", "add", "freetype-dev"]
RUN ["apk", "--no-cache", "add", "lcms2-dev"]
RUN ["apk", "--no-cache", "add", "libwebp-dev"]
RUN ["apk", "--no-cache", "add", "tcl-dev"]
RUN ["apk", "--no-cache", "add", "tk-dev"]
RUN ["apk", "--no-cache", "add", "harfbuzz-dev"]
RUN ["apk", "--no-cache", "add", "fribidi-dev"]
RUN ["apk", "--no-cache", "add", "libimagequant-dev"]
RUN ["apk", "--no-cache", "add", "libxcb-dev"]
RUN ["apk", "--no-cache", "add", "libpng-dev"]

# COPY REQUIREMENTS.TXT
COPY ./requirements.txt ./requirements.txt

# INSTALL PYTHON DEPENDENCIES
RUN ["pip", "install", "-r", "requirements.txt"]

# COPY A2J
COPY . .

# OPEN PORT 8080
EXPOSE 8080

# RUN A2J
CMD ["python", "src/main.py"]
