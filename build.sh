#!/bin/bash
# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Print success message
echo "Build completed successfully!"