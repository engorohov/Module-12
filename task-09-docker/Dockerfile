# === stage 1: builder ===
FROM python:3.12-slim AS builder

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --frozen --no-install-project || true

# === stage 2: runtime ===
FROM python:3.12-slim

RUN groupadd --system app && \
    useradd --system --gid app --no-create-home app

WORKDIR /app

COPY --chown=app:app app.py ./

USER app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

CMD ["python", "app.py"]
