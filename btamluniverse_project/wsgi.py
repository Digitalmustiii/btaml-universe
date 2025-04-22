import os
from django.core.wsgi import get_wsgi_application

# Standard WSGI entrypoint for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btamluniverse_project.settings")
application = get_wsgi_application()

# Add WhiteNoise for static file serving
from whitenoise import WhiteNoise
static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles')
application = WhiteNoise(application)
# Remove the makedirs line that was causing the error
application.add_files(static_path, prefix='static/')

app = application  # For Vercel