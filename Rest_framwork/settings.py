"""
Django settings for Rest_framwork project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import pymysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hskt@(8dymfpr6)3=n5pmrzdc*fc64s%!klzm1gq^qm@^brrn*'

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
    'classbaseview',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Rest_framwork.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Rest_framwork.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
         'NAME': 'restframwork', #数据库名称
         'USER':'root', # 连接数据库的用户名称
         'PASSWORD':'123456',  # 用户密码
         'HOST':'127.0.0.1', # 访问的数据库的主机的ip地址
         'PORT':'3306', # 默认mysql访问端口
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

# 认证 权限 节流 全局配置
REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    #全局认证
    # "DEFAULT_AUTHENTICATION_CLASSES":["classbaseview.auth.Authication1","classbaseview.auth.Authication"],
    # "DEFAULT_AUTHENTICATION_CLASSES": ["classbaseview.util.Authication.Authication"],
    #匿名用户配置
    # "UNAUTHENTICATED_USER":None,
    # "UNAUTHENTICATED_TOKEN":None,
    # "DEFAULT_THROTTLE_RATES":{
    #     "hq":"3/m",
    #     "user":"4/m"
    # },
    # "VERSION_PARAM":"version",
    # "DEFAULT_VERSION":"v1",
    # "ALLOWED_VERSIONS":["v1","v2"]

}
