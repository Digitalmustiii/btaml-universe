import os
import sys

# ── Auto‐collect static on Vercel cold start ─────────────────────────────────────
if os.getenv('VERCEL'):
    # Add project root to path so manage.py commands work
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btamluniverse_project.settings')
    from django.core.management import call_command
    # Collect static into STATIC_ROOT (staticfiles/) with zero output
    call_command('collectstatic', '--noinput', verbosity=0)

# ── Usual WSGI setup ─────────────────────────────────────────────────────────────
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btamluniverse_project.settings')
application = get_wsgi_application()
