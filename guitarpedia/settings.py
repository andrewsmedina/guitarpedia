import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'banco.db'

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = ''

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'cn%68nehi(_e68wyfsurt*q+$-qub-0#6bh142q=0%p-5tjmoh'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'guitarpedia.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates")
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    
    'south',
    
    'artists',
    'home',
)
