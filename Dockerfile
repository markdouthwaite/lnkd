FROM python:3.7.2

ENV POETRY_VERSION=1.0.5

COPY . /pkg

WORKDIR /pkg

RUN pip install -U pip && pip install poetry==$POETRY_VERSION
RUN python -m venv /venv && /venv/bin/pip install -U pip

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

RUN poetry build && /venv/bin/pip install dist/*.whl
