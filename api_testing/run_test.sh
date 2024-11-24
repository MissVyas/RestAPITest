#!/bin/bash

# Create logs directory
mkdir -p logs

# Run the tests in a Docker container
docker build -t api-testing .
docker run --rm -v "$(pwd)/logs:/tests/logs" api-testing
