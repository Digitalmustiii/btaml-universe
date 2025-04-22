import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btamluniverse_project.settings")
application = get_wsgi_application()

# Expose the WSGI application as "app" and "handler" for Vercel
app = application
handler = application
