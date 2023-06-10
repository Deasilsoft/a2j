FROM python:3.9-alpine

LABEL version="2023.06"
LABEL description="Deasilsoft/a2j"
LABEL maintainer="Sondre Benjamin Aasen"

# setup timezone
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install dependencies
RUN apk --no-cache add \
    build-base \
    curl \
    freetype-dev \
    harfbuzz-dev \
    fribidi-dev \
    jpeg-dev \
    lcms2-dev \
    libimagequant-dev \
    libpng-dev \
    libwebp-dev \
    libxcb-dev \
    openjpeg-dev \
    openssl \
    pkgconf \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev

# setup user, group, and home directory
ENV GROUP=a2j \
    USER=a2j \
    HOME=/home/a2j

RUN addgroup -S ${GROUP} && adduser -S ${USER} -G ${GROUP} -h ${HOME}
USER ${USER}
WORKDIR ${HOME}

# setup virtual environment
ENV VENV=/home/a2j/venv
RUN python -m venv ${VENV}
ENV PATH="${VENV}/bin:${PATH}"

# install python dependencies
RUN pip install --no-cache-dir wheel
COPY requirements requirements
ARG ENV=production
RUN pip install --no-cache-dir -r requirements/${ENV}.txt

# copy source code
COPY --chown=${USER}:${GROUP} . .

# set environment variables for flask
ENV FLASK_APP=/home/a2j/src/app.py
ENV FLASK_ENV=${ENV}

# expose port, set healthcheck, and run flask
EXPOSE 5000
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1
CMD ["flask", "run", "--host=0.0.0.0"]
