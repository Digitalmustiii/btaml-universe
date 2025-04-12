import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Load secret key from environment variable. Fallback is a dummy default.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG should be False in production.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS - load from an environment variable as a comma-separated string.
# In production, set this to your deployed domains (e.g., "your-app-name.vercel.app,www.yourdomain.com").
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1, localhost, btamluniverse.vercel.app').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # WhiteNoise middleware to serve static files efficiently in production
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'btamluniverse_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'main' / 'templates'],  # global templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'btamluniverse_project.wsgi.application'

# Database configuration
# Using dj_database_url to load the database configuration from the DATABASE_URL env variable.
# For development, it defaults to using SQLite.
DATABASES = {
    'default': dj_database_url.config(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')
}

# Password validation (you may customize validators as needed)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'
# Location of your project's static files for collecting via collectstatic.
STATICFILES_DIRS = [BASE_DIR / 'main' / 'static']
# Directory where static files will be collected.
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Use WhiteNoise to serve compressed static files.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Production Security Settings (uncomment or adjust these if deploying in production)
if not DEBUG:
    # Ensure all traffic is redirected to HTTPS.
    SECURE_SSL_REDIRECT = False
    # Set HSTS headers.
    SECURE_HSTS_SECONDS = 31536000  # one year in seconds
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    # Cookie security
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    # Additional secure settings
    SECURE_CONTENT_TYPE_NOSNIFF = False
