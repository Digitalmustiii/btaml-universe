import os
from django.core.wsgi import get_wsgi_application

# Standard WSGI entrypoint for Django with 'app' exposed for Vercel
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btamluniverse_project.settings")
app = get_wsgi_application()
