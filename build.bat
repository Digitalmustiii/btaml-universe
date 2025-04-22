@echo off
REM Install Python dependencies
pip install -r requirements.txt

REM Collect static files
python manage.py collectstatic --noinput

REM Print success message
echo Build completed successfully!