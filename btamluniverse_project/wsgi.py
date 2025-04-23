import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btamluniverse_project.settings")

# Standard Django WSGI app
application = get_wsgi_application()

# Let WhiteNoise serve /static/ from STATIC_ROOT
application = WhiteNoise(application, root=str(application.settings.STATIC_ROOT), prefix='static/')

# Also expose as `app` for Vercel’s runtime
app = application
