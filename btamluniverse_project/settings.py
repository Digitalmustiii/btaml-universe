import os
from pathlib import Path
import environ
import environ
import dj_database_url

# ── BASE DIR ───────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ── ENVIRONMENT VARIABLES ─────────────────────────────────────────────────────
# 1) Define the env, including any casting and defaults:

# 1) Initialize environment variables with casting and defaults
env = environ.Env(
    DEBUG=(bool, False),  # Default False for DEBUG
    EMAIL_USE_TLS=(bool, True),  # Default True for EMAIL_USE_TLS
    DATABASE_URL=(str, ''),  # Define DATABASE_URL explicitly as str
)

# 2) Read the .env file from project root (adjust BASE_DIR accordingly)
env.read_env(os.path.join(BASE_DIR, '.env'))

# ── SECURITY ───────────────────────────────────────────────────────────────────
SECRET_KEY   = env('DJANGO_SECRET_KEY', default='your-default-secret-key')
DEBUG        = False
ALLOWED_HOSTS = [
    'btamluniverse.vercel.app',
    'vercel.app',
    '127.0.0.1',
]


# ── APPLICATION DEFINITION ────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main.apps.MainConfig',
    'django_ckeditor_5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'btamluniverse_project.urls'
WSGI_APPLICATION = 'btamluniverse_project.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'main' / 'templates'],
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

# ── DATABASE ───────────────────────────────────────────────────────────────────

import dj_database_url

# Database settings
DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL'),  # Use the DATABASE_URL from env
        conn_max_age=600,
        ssl_require=True
    )
}

# ── PASSWORD VALIDATION ────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── INTERNATIONALIZATION & TIME ────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'UTC'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# ── STATIC & MEDIA ─────────────────────────────────────────────────────────────
# Replace your current STATIC settings with these
# Serve directly from your GitHub via jsDelivr:
STATIC_URL = "https://Digitalmustiii.github.io/btamluniverse/"



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ── CKEDITOR 5 ─────────────────────────────────────────────────────────────────
# ── CKEDITOR 5 ─────────────────────────────────────────────────────────────────
# ── EMAIL (via .env) ───────────────────────────────────────────────────────────
EMAIL_BACKEND      = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST         = env('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT         = env('EMAIL_PORT', default=587)
EMAIL_USE_TLS      = env('EMAIL_USE_TLS')
EMAIL_HOST_USER    = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD= env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ── DEFAULT PRIMARY KEY TYPE ──────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
