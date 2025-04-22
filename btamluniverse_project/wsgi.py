import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btamluniverse_project.settings")

application = get_wsgi_application()

app = application

if os.environ.get('VERCEL'):
    os.system("bash vercel_build.sh")