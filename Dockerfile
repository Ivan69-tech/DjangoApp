FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y gcc build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . code

WORKDIR /code/graph

EXPOSE 5555

CMD ["daphne", "-p", "5555", "--bind", "0.0.0.0", "graph.asgi:application"]


