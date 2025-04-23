#!/bin/bash
echo "Building static files..."
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput