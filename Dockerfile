FROM python:3.10-alpine

RUN apk update && apk add \
        postgresql-dev \
        build-base \
        pcre-dev \
        gcc \
        jpeg-dev \
        zlib-dev \
        musl-dev \
        libc-dev \
        linux-headers && \
        mkdir app

WORKDIR /app/

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1
ADD . /app/
ADD ./requirements.txt /
RUN pip install -r requirements.txt

