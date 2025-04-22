#!/usr/bin/env bash
set -e

# install Python deps so collectstatic can run
pip install -r requirements.txt

# collect static into your distDir
python btamluniverse_project/manage.py collectstatic --noinput

# move the generated static into staticfiles_build/
# (adjust this if collectstatic writes elsewhere)
mv btamluniverse_project/static/ staticfiles_build
