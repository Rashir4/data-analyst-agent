# Stage: Python app
FROM python:3.12-slim
ENV PYTHONPATH /data-analyst-agent
# Minimal build deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.2
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# ─── Copy & install Python deps ─────────────────────────────────────
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry install

# ─── Copy project code ──────────────────────────────────────────────
COPY . /app

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"]
