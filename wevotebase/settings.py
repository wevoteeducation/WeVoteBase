# wevotebase/settings.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

"""
Django settings for wevotebase project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import logging
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(-ack%@p)$dpr-4*q$a@ir%64(_(q6!ve@=r&5i*@-fw6bjnqq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Comment out when running Heroku
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'bootstrap3',
    'social.apps.django_app.default',
    # 'crispy_forms',

    # project specific
    'election_office_measure',
    'exception',
    'follow',
    'import_export',
    'import_export_azavea_cicero',
    'import_export_google_civic',
    'import_export_maplight',
    'import_export_theunitedstatesio',
    'import_export_twitter',
    'import_export_voting_info_project',
    'organization',
    'politician',
    'position',
    'region_jurisdiction',
    'rest_framework',
    'support_oppose_deciding',
    'tag',
    'twitter',
    'utils',
    'ux_birch',
    'ux_oak',  # The business logic for this particular version of We Vote
    'wevote_functions',
    'wevote_settings',
    'wevote_social',
    'voter',  # See also AUTH_USER_MODEL in wevotebase/settings.py
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'wevote_social.middleware.SocialMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'wevotebase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'wevotebase/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # Django Cookbook
                'django.template.context_processors.static',  # Django Cookbook
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'wevote_social.context_processors.profile_photo',
            ],
        },
    },
]

WSGI_APPLICATION = 'wevotebase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# Comment out these lines when running Heroku
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'WeVoteDB',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',  # localhost
        'PORT': '',  # 5432
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Described here: https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#a-full-example
AUTH_USER_MODEL = 'voter.Voter'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, "wevotebase", "static")  # Django Cookbook
MEDIA_URL = '/media/'  # Django Cookbook
MEDIA_ROOT = os.path.join(PROJECT_PATH, "wevotebase", "media")  # Django Cookbook

# We want to default to cookie storage of messages so we don't overload our app servers with session data
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Default settings described here: http://django-bootstrap3.readthedocs.org/en/latest/settings.html
BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set HTML disabled attribute on disabled fields
    'set_disabled': False,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}

LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_FACEBOOK_KEY = '868492333200013'
SOCIAL_AUTH_FACEBOOK_SECRET = '6789422f725299afe12bf271ebb59d6b'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_friends']
SOCIAL_AUTH_TWITTER_KEY = 'iMJMr4WrR4F5PLkuwrC3gDkFf'
SOCIAL_AUTH_TWITTER_SECRET = '9kVeY7UEWRDOeagvdHNLsAYumgeWYuEWIGRxNK3k3r28qZ6YXr'
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

########### Logging configurations ###########
#   LOG_STREAM          Boolean     True will turn on stream handler.
#   LOG_FILE            String      Path to file to write to. Make sure executing
#                                   user has permissions.
#   LOG_STREAM_LEVEL    Integer     Log level of stream handler.
#   LOG_FILE_LEVEL      Integer     Log level of file handler.

LOG_STREAM = True
LOG_FILE = None
#LOG_FILE = "/var/log/wevote/wevote.log"
LOG_STREAM_LEVEL = logging.INFO
LOG_FILE_LEVEL = logging.ERROR

########### Heroku Settings ###########
# Comment out to run database locally

# #Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES = {}
# DATABASES['default'] = dj_database_url.config()
#
# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
# # Allow all host headers
# ALLOWED_HOSTS = ['*']
#
# # Static asset configuration
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
