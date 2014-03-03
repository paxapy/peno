# coding=utf-8
from settings import *

DEBUG = True

CMS_TEMPLATES = (
    ('base.html', u'Обычный'),
    ('index.html', u'Главная'),
)

INSTALLED_APPS += (
    'djangocms_text_ckeditor',
    'djangocms_picture',

    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'djangocms_admin_style',
    'easy_thumbnails',
    'django.contrib.messages',
    'django.contrib.sites',

    'app',
)

MIDDLEWARE_CLASSES += (
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
)

SITE_ID = 1

LANGUAGES = [
    ('ru', u'Русский'),
]