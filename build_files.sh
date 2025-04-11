#!/bin/bash
echo "Building static files"
python manage.py collectstatic --noinput

# Make this file executable
chmod +x build_files.sh