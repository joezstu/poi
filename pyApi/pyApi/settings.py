"""
Django settings for pyApi project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import djcelery
from celery.schedules import timedelta, crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ump%z+ulc-(k)ep+2_zv0sh#md^be&8%1n%d-be0=yyp8hez*k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # 'djcelery'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 注册中间件
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pyApi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'pyApi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

STATIC_URL = '/upload/'
#
# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = [
#     'http://py.poi.com:8080',
#     'http://localhost:8080'
# ]
# CORS_ALLOW_HEADERS = (
#     "*"
# )


# 改变你的表单指向py.poi.com:8000/import/(注意末尾的斜杠)，或者在Django设置中设置APPEND_SLASH=False。
APPEND_SLASH = True

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# 使用redis代理来分发任务
# BROKER_URL = 'redis://127.0.0.1:6379/8'
# CELERY_IMPORTS = ('CeleryTask.tasks')  # 导入任务，可以执行的异步任务
# CELERY_TIMEZONE = 'Asia/Shanghai'  # 中国时区
# CELERYBEAT_SCHEDULER='djcelery.schduler.DatabaseScheduler'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False if DEBUG else True,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)s %(message)s'
            # "class": "pythonjsonlogger.jsonlogger.JsonFormatter"
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(lineno)d %(message)s'
            # "class": "pythonjsonlogger.jsonlogger.JsonFormatter"
        },  # 日志记录级别+时间日期+模块名称+函数名称+行号+记录消息
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'DEBUG' if DEBUG else 'INFO',
            'filters': ['require_debug_true'],  # debug为true才会输出
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'info': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(str(BASE_DIR) + '/logs/', "info.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,  # 300M大小
            'backupCount': 10,
            'formatter': 'verbose',
            'encoding': 'utf-8'
        },


    },
    'loggers': {  # 日志器
        "django": {  # 默认的logger应用如下配置
            "handlers": ["info", "console"],
            "propagate": True,
            "level": "INFO"
        },

    }
}

STATICFILES_DIRS = (('upload',os.path.join(BASE_DIR, 'upload/')))