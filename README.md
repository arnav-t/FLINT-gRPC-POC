# FLINT gRPC POC

## Running the server in docker

1. `docker build -t flint-grpc .`
2. `docker run --rm -p 50051:50051 flint-grpc`

## Running the server sans Docker (requires FLINT)

1. `make install`
2. `make`
3. `python3 app.py`

## Use client

1. `python3 client.py`