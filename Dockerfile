FROM python:3.12-trixie
WORKDIR /app
COPY uv.lock ./uv.lock
COPY pyproject.toml ./pyproject.toml
COPY README.md ./README.md
COPY api ./api
COPY src ./src
COPY models ./models

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN uv sync

CMD ["uv", "run", "uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "8080"]
