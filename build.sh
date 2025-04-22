@echo off

REM Install Python dependencies
pip install -r requirements.txt

REM Collect static files into the STATIC_ROOT directory
python manage.py collectstatic --noinput

REM Add any other necessary commands here
