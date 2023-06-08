# BUILD FROM PYTHON:ALPINE
FROM python:3-alpine3.18

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

# CREATE AND SET GROUP, USER AND WORK DIRECTORY
ENV GROUP=a2j
ENV USER=a2j
ENV HOME=/home/a2j
RUN addgroup -S ${GROUP} && adduser -S ${USER} -G ${GROUP} -h ${HOME}
USER ${USER}
WORKDIR ${HOME}

# SETUP THE VIRTUAL ENVIRONMENT AND UPDATE PATH TO PRIORITIZE THE VIRTUAL ENVIRONMENT
ENV VENV=/home/a2j/venv
RUN python -m venv ${VENV}
ENV PATH="${VENV}/bin:${PATH}"

# INSTALL WHEEL TO INCREASE SPEED
RUN pip install --no-cache-dir wheel

# COPY REQUIREMENTS
COPY requirements requirements

# GET ENVIRONMENT
ARG ENV=production

# INSTALL PYTHON DEPENDENCIES
RUN pip install --no-cache-dir -r requirements/${ENV}.txt

# COPY ALL AVAILABLE FILES
COPY --chown=${USER}:${GROUP} . .

# PREPARE FLASK
ENV FLASK_APP=/home/a2j/src/app.py
ENV FLASK_ENV=${ENV}

# EXPOSE PORT 5000 TO LOCAL NETWORK
EXPOSE 5000

# RESTART CONTAINER IF HEALTHCHECK FAILS
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1

# RUN A2J APP
ENTRYPOINT flask run --host=0.0.0.0
