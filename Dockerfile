FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system --ignore-pipfile --verbose

ARG PROJECT_DIR=/app

RUN mkdir -p ${PROJECT_DIR}/data && chmod 777 ${PROJECT_DIR}/data

COPY . .

RUN useradd -m apiuser && chown -R apiuser:apiuser ${PROJECT_DIR} && chmod -R 755 ${PROJECT_DIR}/data

USER apiuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
