#!/usr/bin/env bash
set -e

# Install Python dependencies so collectstatic can run
pip install -r requirements.txt

# Collect static files into the STATIC_ROOT directory (which should be staticfiles)
python btamluniverse_project/manage.py collectstatic --noinput
