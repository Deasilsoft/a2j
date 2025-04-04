FROM python:3.13.2-alpine

LABEL version="2023.06-2"
LABEL description="Deasilsoft/a2j"
LABEL maintainer="Sondre Benjamin Aasen"

ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

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

ARG ENV=production

ENV GROUP=a2j \
    USER=a2j \
    ENV=${ENV} \
    HOME=/home/a2j \
    FLASK_DEBUG=0

ENV VENV=${HOME}/venv
ENV PATH="${VENV}/bin:${PATH}"
ENV FLASK_APP=${HOME}/src/app.py

RUN if [ "${ENV}" = "development" ]; then \
        export FLASK_DEBUG=1; \
    fi

RUN addgroup -S ${GROUP} && adduser -S ${USER} -G ${GROUP} -h ${HOME}

USER ${USER}
WORKDIR ${HOME}

RUN python -m venv ${VENV}
COPY requirements requirements
RUN ${VENV}/bin/pip install --no-cache-dir wheel && \
    ${VENV}/bin/pip install --no-cache-dir -r requirements/${ENV}.txt

COPY --chown=${USER}:${GROUP} . .

EXPOSE 5000

HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1
CMD ["flask", "run", "--host=0.0.0.0"]
