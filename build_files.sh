#!/bin/bash
echo "Building static files..."
/opt/vercel/python3/bin/python -m pip install -r requirements.txt
/opt/vercel/python3/bin/python manage.py collectstatic --noinput