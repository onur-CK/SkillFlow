"""
Django settings for skillflow project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from .env file
# Source: https://pypi.org/project/python-dotenv/
load_dotenv()

# Set DEBUG based on environment variable
# Source: https://docs.djangoproject.com/en/5.1/ref/settings/#debug
DEBUG = os.environ.get("DEBUG", "False") == "True"

# Production security settings
# Source: https://docs.djangoproject.com/en/5.1/topics/security/
if not DEBUG:  # Production settings
    # Forces HTTPS
    SECURE_SSL_REDIRECT = True
    # Ensures the request is through HTTPS
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    # HSTS settings
    # Source: https://docs.djangoproject.com/en/5.1/ref/middleware/#http-strict-transport-security
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # XSS Filter
    SECURE_BROWSER_XSS_FILTER = True
    # Cookie settings
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Security headers
    X_FRAME_OPTIONS = "DENY"
    CSRF_COOKIE_HTTPONLY = True
    SECURE_REFERER_POLICY = "same-origin"
    SECURE_CONTENT_TYPE_NOSNIFF = True
else:  # Development settings
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

# Build paths inside the project
# Source Links: https://docs.djangoproject.com/en/5.1/ref/settings/#base-dir
# https://stackoverflow.com/questions/63844611/how-to-set-django-template-path-properly
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key configuration
# Source: https://docs.djangoproject.com/en/5.1/ref/settings/#secret-key
SECRET_KEY = os.getenv("SECRET_KEY")

# Allowed hosts configuration
# Source: https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "skillflow-community-django-7358f56ac457.herokuapp.com",
    "localhost",
    "127.0.0.1",
]

# Application definition
# Source: https://docs.djangoproject.com/en/5.1/ref/applications/
# https://stackoverflow.com/questions/34377237/how-does-it-work-the-naming-convention-for-django-installed-apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "skillflow",
]

# Middleware configuration
# Source: https://docs.djangoproject.com/en/5.1/topics/http/middleware/
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # For static file serving
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL configuration
ROOT_URLCONF = "skillflow.urls"

# Template configuration
# Source: https://docs.djangoproject.com/en/5.1/topics/templates/
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI configuration
WSGI_APPLICATION = "skillflow.wsgi.application"

# Database configuration
# Source: https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# Using dj-database-url for database configuration
# Source: https://pypi.org/project/dj-database-url/
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"), conn_max_age=600, ssl_require=True
    )
}

# Password validation
# Source: https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files configuration (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# WhiteNoise configuration for static file serving
# Source: http://whitenoise.evans.io/en/stable/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Authentication URLs
# Source: https://docs.djangoproject.com/en/5.1/ref/settings/#login-url
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "about_us"
