"""
Django settings for fashion_main project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hik^k_s#01j*x5x2o4uh+qavw8uu(9=ia248169pae4ixscu_9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'category',
    'accounts',
    'business',
    'smart_selects',
    'ckeditor',
    'products',
    'mptt',
    'carts',
    'django.contrib.humanize',
    'django_dnf',
    'newsletters',
    'contacts',
    'django.contrib.sites',
    'regional_managers',
    'orders',
    'jquery',
    'djangoformsetjs',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fashion_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.category_names',
                'carts.context_processors.counter',
                'products.context_processors.wish_counter',
                'products.context_processors.compare_counter_header',
                'products.context_processors.max_product_price',
                'accounts.context_processors.get_business',
                'carts.context_processors.shopcart_context',
                'products.context_processors.search_products',
            ],
        },
    },
]

WSGI_APPLICATION = 'fashion_main.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fashion_db_04',
        'USER': 'postgres',
        'PASSWORD': 'qWerty@123',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'fashion_main/static'),
]

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

USE_DJANGO_JQUERY = True


# Django messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


# Email sending
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rathan.kumar049@gmail.com'
EMAIL_HOST_PASSWORD = 'Giveme99$'
EMAIL_USE_TLS = True


# Mailchimp Configuration
# Docs at: https://mailchimp.com/developer/guides/marketing-api-conventions/
# https://mailchimp.com/developer/api/marketing/lists/
MAILCHIMP_API_KEY = 'cf7f2f57092893b3c75c661a56a00bb7-us7'
MAILCHIMP_DATA_CENTER = 'us7'
MAILCHIMP_EMAIL_LIST_ID = 'bf99cd038c'
