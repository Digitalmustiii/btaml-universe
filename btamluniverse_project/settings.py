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
    'btamluniverse.pythonanywhere.com',
    'btamluniverse.vercel.app',
    'vercel.app',
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
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ── CKEDITOR 5 ─────────────────────────────────────────────────────────────────
# ── CKEDITOR 5 ─────────────────────────────────────────────────────────────────
CKEDITOR_5_UPLOAD_PATH = "uploads/"

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading', '|',
                'bold', 'italic', 'underline', '|',
                'uploadFile',    # ← Generic file upload button
                'imageUpload',   # ← Image upload
                'link',          # ← Hyperlinks
                'bulletedList', 'numberedList', '|',
                'insertTable',   # ← Tables
                'mediaEmbed',    # ← Video embed
                'fontFamily', 'fontSize', '|',
                'fontColor', '|',
                'undo', 'redo'
            ],
            'shouldNotGroupWhenFull': False,
        },

        # Simple Upload Adapter config
        # this URL must point to your Django view that saves the file and returns JSON { "url": "<file-url>" }
        'simpleUpload': {
            'uploadUrl': '/ckeditor/upload/',
            'headers': {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        },

        # Table plugin
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells'
            ]
        },

        # Headings
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph'},
                {'model': 'heading1',  'view': 'h1', 'title': 'Heading 1'},
                {'model': 'heading2',  'view': 'h2', 'title': 'Heading 2'},
            ]
        },

        # Font & color
        'fontFamily': {
            'options': [
                'default','Arial, Helvetica, sans-serif','Georgia, serif',
                'Tahoma, Geneva, sans-serif','Courier New, Courier, monospace'
            ]
        },
        'fontSize': {'options': [10,12,14,'default',18,24,32]},
        'fontColor': {
            'columns': 3,
            'colors': [
                {'color':'hsl(0,0%,0%)','label':'Black'},
                {'color':'hsl(0,75%,60%)','label':'Red'},
                {'color':'hsl(204,76%,53%)','label':'Blue'},
                {'color':'hsl(120,75%,60%)','label':'Green'},
            ]
        },

        # Media embed & image
        'mediaEmbed': {'previewsInData': True},
        'image': {'toolbar': ['imageTextAlternative','imageStyle:full']},

        'height': 300, 'width': '100%',
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
