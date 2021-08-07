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
ENV GROUP=a2j
ENV USER=a2j
ENV HOME=/home/a2j
ENV VENV=/home/a2j/venv
ENV FLASK_APP=/home/a2j/src/app.py
ENV FLASK_ENV=development

# CREATE GROUP AND USER
RUN addgroup -S ${GROUP} && adduser -S ${USER} -G ${GROUP} -h ${HOME}

# SET USER AND WORK DIRECTORY
USER ${USER}
WORKDIR ${HOME}

# SETUP THE VIRTUAL ENVIRONMENT
RUN python -m venv ${VENV}

# UPDATE PATH TO INCLUDE AND PRIORITIZE THE VIRTUAL ENVIRONMENT
ENV PATH="${VENV}/bin:${PATH}"

# COPY REQUIREMENTS
COPY requirements requirements

# INSTALL PYTHON DEPENDENCIES
RUN pip install --no-cache-dir -r requirements/${FLASK_ENV}.txt

# COPY ALL FILES (except directories & files listed in .dockerignore)
COPY --chown=${USER}:${GROUP} . .

# EXPOSE PORT 5000 TO LOCAL NETWORK
EXPOSE 5000

# RESTART CONTAINER IF HEALTHCHECK FAILS
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1

# RUN A2J APP
CMD flask run --host=0.0.0.0
