import os
from pathlib import Path

import environ
import dj_database_url

# ── BASE DIR ───────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ── ENVIRONMENT VARIABLES ─────────────────────────────────────────────────────
# 1) Define the env, including any casting and defaults:
env = environ.Env(
    DEBUG       = (bool, False),
    EMAIL_USE_TLS = (bool, True),
)

# 2) Read the .env file from project root:
env.read_env(os.path.join(BASE_DIR, '.env'))

# ── SECURITY ───────────────────────────────────────────────────────────────────
SECRET_KEY   = env('DJANGO_SECRET_KEY', default='your-default-secret-key')
DEBUG        = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])

# If you deploy on Railway, for example:
if env('RAILWAY_URL', default=None):
    ALLOWED_HOSTS.append(env('RAILWAY_URL'))

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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'
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
STATIC_URL           = '/static/'
STATICFILES_DIRS     = [BASE_DIR / 'static']
STATIC_ROOT          = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE  = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL            = '/media/'
MEDIA_ROOT           = BASE_DIR / 'media'

# ── CKEDITOR 5 ─────────────────────────────────────────────────────────────────
CKEDITOR_5_UPLOAD_PATH = "uploads/"
CKEDITOR_5_CONFIGS     = {
    'default': {
        # your toolbar, font configs, etc…
    }
}

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
