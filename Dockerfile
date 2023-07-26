FROM python:3.9-slim as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

RUN mkdir -p /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        make

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH "${PATH}:/root/.local/bin"

RUN poetry config virtualenvs.create false


COPY pyproject.toml poetry.lock ./
RUN poetry install  --no-interaction --no-ansi

ADD . /app
ENV DJANGO_SETTINGS_MODULE="it_bootcamp.settings"

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000