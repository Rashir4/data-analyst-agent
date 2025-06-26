# Stage: Python app
FROM python:3.12-slim
ENV PYTHONPATH /data-analyst-agent
# Minimal build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/var/cache/pypoetry \
    POETRY_HOME='usr/local/' 
RUN pip install poetry

# ─── Copy & install Python deps ─────────────────────────────────────
WORKDIR /app
COPY . /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry lock
RUN poetry install --no-ansi --no-root


EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]
