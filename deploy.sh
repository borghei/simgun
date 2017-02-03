#!/bin/bash

set -e

# Build image
docker-compose build
# Run container
docker-compose up -d