"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from config import secret_keys
import sys
sys.modules['django.utils.six.moves.urllib.parse'] = __import__('six.moves.urllib_parse',
fromlist=['urlencode'])
sys.modules['django.utils.six.moves.urllib.request'] = __import__('six.moves.urllib_request',
fromlist=['urlopen'])
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iw21*r23)5j$la5wt((&!w3rni1u^+uf_1nljfzthr!%5oee-s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1','.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'notice',
    'c_type',
    'storages',
    'disqus', #댓글 앱
    'django.contrib.sites', #사이트 관리 프레임워크
    'accounts',
    'photo',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recommendApp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DATABASES['default'].update(dj_database_url.config(conn_max_age=500)) #db엑세스타임변경

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


LOGIN_REDIRECT_URL = '/' # 로그인 이후에 이동되는 페이지는 profile페이지이다. 이것을 바꿔준 것.

DISQUS_WEBSITE_SHORTNAME = 'ddobagi'
SITE_ID = 1

AWS_ACCESS_KEY_ID = secret_keys.keys.access_key
AWS_SECRET_ACCESS_KEY = secret_keys.keys.secret_access_key
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'ddobagi'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)

AWS_S3_FILE_OVERWIRTE = False
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl' : 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'

STATIC_URL = 'http://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

DEFAULT_FILE_STORAGE = 'config.s3media.MediaStorage'
# #다음에 만들 MediaStorage라는 클래스를 통해 파일 저장소를 사용하겠다.

# 배포
# pip install dj-database-url ->데이터베이스 환경변수를 설정할 수 있게 해주는 유틸리티
# pip install gunicorn ->wsgi미들웨어
# pip install whitenoise -> 정적 파일의 사용을 돕는 미들웨어
# pip install psycopg2-binary -> PostgreSQL사용을 위한 모듈
# pip freeze > requirements.txt -> 필요한 모듈들을 모아줌