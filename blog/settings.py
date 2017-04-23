"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%k0hlk@%4oq-_1e40)^bf!-77m9+uai#mi9d54)b8dves@ey-r'

# SECURITY WARNING: don't run with debug turned on in production!
# 使用到生产环境要把DEBUG改为FALSE
DEBUG = True

if DEBUG:
    # 根据DEBUG来确定
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS = (
    # 原来自带的
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 添加使用manage.py生成的app
    # 博客应用
    'blog_articles',
    # 留言板应用
    'msb',
    # 加入通过pip安装的包
    # 分别有markdown2,markdown_deux,pagedown
    'markdown2',
    'markdown_deux',
    # Markdown编辑器
    'draceditor',
    # crispy-forms
    'crispy_forms',
    'bootstrapform',
    # el_pagination分页插件
    'el_pagination',

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
)

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 使用mysql替换自带的sqlite3
        # 写完这些信息之后执行python manage.py migrate进行迁移
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# 设置中文
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
# 时区设置为北京时间
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# 设置静态资源目录
STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 静态文件搜索顺序
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

EL_PAGINATION_PER_PAGE = 1
EL_PAGINATION_FIRST_LABEL = 'First'
EL_PAGINATION_LAST_LABEL = 'Last'
EL_PAGINATION_NEXT_LABEL = 'Next'
EL_PAGINATION_PREVIOUS_LABEL = 'Prev'
