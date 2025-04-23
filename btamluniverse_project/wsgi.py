import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btamluniverse_project.settings")
application = get_wsgi_application()

# Add WhiteNoise without trying to modify the filesystem
from whitenoise import WhiteNoise
application = WhiteNoise(application)
application.add_files('static', prefix='static/')

# For Vercel
app = application