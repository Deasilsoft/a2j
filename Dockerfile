FROM python:alpine

# INSTALL PREREQUISITES TO PYTHON DEPENDENCIES
RUN apk --no-cache add build-base \
                       curl \
                       tiff-dev \
                       jpeg-dev \
                       openjpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       libwebp-dev \
                       tcl-dev \
                       tk-dev \
                       harfbuzz-dev \
                       fribidi-dev \
                       libimagequant-dev \
                       libxcb-dev \
                       libpng-dev

# SET ENVIRONMENT VARIABLES
ENV A2J_GROUP=a2j
ENV A2J_USER=a2j
ENV A2J_HOME=/home/a2j
ENV FLASK_ENV=development

# CREATE GROUP AND USER
RUN addgroup -S ${A2J_GROUP} && adduser -S ${A2J_USER} -G ${A2J_GROUP} -h ${A2J_HOME}

# SET USER AND WORK DIRECTORY
USER ${A2J_USER}
WORKDIR ${A2J_HOME}

# COPY REQUIREMENTS.TXT
COPY ./requirements.txt ./requirements.txt

# INSTALL PYTHON DEPENDENCIES
RUN pip install --no-cache-dir -r requirements.txt

# COPY A2J
COPY --chown=${A2J_USER}:${A2J_GROUP} . .

# OPEN PORT 8080
EXPOSE 8080

# RESTART CONTAINER IF HEALTHCHECK FAILS
HEALTHCHECK CMD curl --fail http://localhost:8080 || exit 1

# RUN A2J
CMD python src/main.py
