import os
from django.core.wsgi import get_wsgi_application

# Standard WSGI entrypoint for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btamluniverse_project.settings")
application = get_wsgi_application()

# Add WhiteNoise for static file serving
from whitenoise import WhiteNoise
application = WhiteNoise(application)
static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles')
if not os.path.exists(static_path):
    os.makedirs(static_path, exist_ok=True)
application.add_files(static_path, prefix='static/')

# For Vercel
app = application