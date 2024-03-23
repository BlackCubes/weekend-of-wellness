from .base import *

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

# NOTE: For now until we think about upgrading the account in PythonAnywhere to
# support PostgreSQL.
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": os.getenv("DATABASE_NAME"),
#         "USER": os.getenv("DATABASE_USER"),
#         "PASSWORD": os.getenv("DATABASE_PASSWORD"),
#         "HOST": os.getenv("DATABASE_HOST"),
#         "PORT": os.getenv("DATABASE_PORT"),
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

ALLOWED_HOSTS = (
    "weekendofwellness.pythonanywhere.com",
    "www.weekendofwellness.pythonanywhere.com",
    "kingsburgwellness.com",
    "www.kingsburgwellness.com",
)
CSRF_TRUSTED_ORIGINS = (
    "https://weekendofwellness.pythonanywhere.com",
    "https://kingsburgwellness.com/",
    "https://www.kingsburgwellness.com/",
)

# WHITENOISE
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, "static"),)
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = (
    "compressor.filters.css_default.CssAbsoluteFilter",
    "compressor.filters.cssmin.CSSMinFilter",
)
COMPRESS_CSS_HASHING_METHOD = "content"

# HSTS SETTINGS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
