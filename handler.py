import os
import sys

# Ensure the project directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'btamluniverse_project.settings')

# Import the WSGI application from your project's WSGI module
from btamluniverse_project.wsgi import application

# Expose the application as 'app' (and optionally 'handler')
app = application
handler = app
