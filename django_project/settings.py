import os
from pathlib import Path
from environs import Env  

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)


DATABASES = {
    'default': env.dj_db_url("DATABASE_URL")
}


ALLOWED_HOSTS = [ #put '*' if u want anyone to run it
'.onrender.com',
'localhost',
'127.0.0.1',
] 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #3rd party
    "crispy_forms",
    "crispy_bootstrap5",
    "whitenoise.runserver_nostatic",
    #rest apis
    "rest_framework",
    #local
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    "articles.apps.ArticlesConfig",
]
TIME_ZONE = 'Asia/Kolkata'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


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

AUTH_USER_MODEL = 'accounts.CustomUser'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_TZ = False

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
CRISPY_ALLOWED_TEMPLATE_PACK="bootstrap5"
CRISPY_TEMPLATE_PACK="bootstrap5"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "farzanfaisal.log.acc@gmail.com"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_HOST_USER = "apikey"
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False