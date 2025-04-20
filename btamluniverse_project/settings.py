import os
from pathlib import Path
import dj_database_url
import environ
import dj_database_url
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Load secret key from environment variable. Fallback is a dummy default.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG should be False in production.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS - load from an environment variable as a comma-separated string.
# In production, set this to your deployed domains (e.g., "your-app-name.vercel.app,www.yourdomain.com").
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
RAILWAY_URL = os.environ.get('RAILWAY_URL')
if RAILWAY_URL:
    ALLOWED_HOSTS.append(RAILWAY_URL)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',  # This line must be present
    "django_ckeditor_5",  # this is for CKEditor 5

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'btamluniverse_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'main/templates' ],  # global templates directory
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
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# optional, but recommended for uploads
CK_EDITOR_5_UPLOAD_PATH = "uploads/"

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
# Add any other directories you want Django to search for static files.
STATICFILES_DIRS = [
     BASE_DIR / 'static',
 ]

# Directory where static files will be collected.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Use the default storage for static files with WhiteNoise.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Static file finders that Django uses to locate static files in your directories and apps.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEditor 5 configuration
# settings.py

# settings.py

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'bold', 'italic', 'underline', 'strikethrough', '|',
            'fontFamily', 'fontSize', '|',
            'fontColor', 'fontBackgroundColor', '|',
            'link', '|',
            'imageUpload', 'mediaEmbed', '|',
            'undo', 'redo'
        ],
        'fontFamily': {
            'options': [
                'default',
                'Arial, Helvetica, sans-serif',
                'Courier New, Courier, monospace',
                'Georgia, serif',
                'Tahoma, Geneva, sans-serif',
                'Trebuchet MS, Helvetica, sans-serif',
                'Verdana, Geneva, sans-serif'
            ]
        },
        'fontSize': {
            'options': [10, 12, 14, 'default', 18, 20, 24, 28, 32]
        },
        'fontColor': {
            'columns': 5,
            'colors': [
                { 'color': 'hsl(0, 0%, 0%)',    'label': 'Black' },
                { 'color': 'hsl(0, 75%, 60%)',  'label': 'Red' },
                { 'color': 'hsl(30, 75%, 60%)', 'label': 'Orange' },
                { 'color': 'hsl(60, 75%, 60%)', 'label': 'Yellow' },
                { 'color': 'hsl(120, 75%, 60%)','label': 'Green' },
                
            ]
        },
        'fontBackgroundColor': {
            'columns': 5,
            'colors': [
                { 'color': 'hsl(0, 0%, 100%)',  'label': 'White',  'hasBorder': True },
                { 'color': 'hsl(0, 0%, 90%)',   'label': 'Light Grey' },
                { 'color': 'hsl(0, 0%, 60%)',   'label': 'Grey' },
                { 'color': 'hsl(0, 75%, 60%)',  'label': 'Red' },
                { 'color': 'hsl(120, 75%, 60%)','label': 'Green' },
                
            ]
        },
        'mediaEmbed': {
            'previewsInData': True
        },
        'height': 400,
        'width': '100%',
    }
}

CKEDITOR_5_UPLOAD_PATH = "uploads/"

#for newsletter
# settings.py
# BASE_DIR = outer project directory (where your .env lives)
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize
env = environ.Env()
env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

# Email settings
EMAIL_BACKEND        = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST           = "smtp.gmail.com"
EMAIL_PORT           = 587
EMAIL_USE_TLS        = True
EMAIL_HOST_USER      = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD  = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL   = EMAIL_HOST_USER

EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="fake@email.com")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="fakepassword")

# Debugging to ensure your email credentials are loading correctly (optional)
#print("Email User:", EMAIL_HOST_USER)
#print("Email Password:", EMAIL_HOST_PASSWORD)

# For production
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')