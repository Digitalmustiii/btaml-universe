import os
import sys

# Ensure the project directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btamluniverse_project.settings')

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()  # Vercel expects this to be named 'app'
