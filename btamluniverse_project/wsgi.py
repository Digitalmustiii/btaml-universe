import os
from django.core.wsgi import get_wsgi_application

# Standard WSGI entrypoint for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btamluniverse_project.settings")
application = get_wsgi_application()

# Add WhiteNoise for static file serving
from whitenoise import WhiteNoise
application = WhiteNoise(application)
application.add_files(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles'), prefix='static/')

app = application  # For Vercel