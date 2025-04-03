#!/bin/bash
# This script is used to start the Docker containers for the application.

docker-compose -f docker-compose.dev.yml up --build --remove-orphans