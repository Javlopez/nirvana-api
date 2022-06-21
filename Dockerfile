ARG VENV=/home/app/.venv

FROM python:3.9-alpine AS base
RUN apk update
LABEL Name="nirvana-api" \
      Vendor="Javier" \
      Description="Nirvana Api fusion"


FROM base AS builder
ARG VENV
RUN apk add bash
RUN adduser -D -s /bin/bash api
USER app
RUN pip install virtualenv
ENV PATH="$VENV/bin:$PATH"
RUN python3.9 -m venv $VENV
WORKDIR /app
RUN pip3 install --upgrade pip setuptools
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app

FROM base as server
ARG VENV
ARG PORT=8000
ENV PORT=${PORT}
RUN adduser --disabled-password --shell /bin/sh api
USER app
COPY --from=builder $VENV $VENV
ENV PATH="$VENV/bin:$PATH"
COPY . /app
WORKDIR /app
LABEL Target="server"
CMD gunicorn --reload --bind 0.0.0.0:${PORT} app:api
