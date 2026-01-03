FROM python:3.12-slim

WORKDIR /code

RUN apt-get update && apt-get install -y \
    build-essential && \
    curl && \
    software-properties-common && \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . /code/

EXPOSE 8000


CMD ["fastapi", "run", "app/main.py", "--port", "80"]