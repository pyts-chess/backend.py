#!/bin/bash

# Export environment variables
export $(grep -v '^#' .env | xargs)

nginx
