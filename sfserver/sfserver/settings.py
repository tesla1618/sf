SECRET_KEY = 'django-insecure-^-3jtazesun-^f+(7c170_k&u%obt(=1j@(1q1pf9ul4xs05wl'
"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


from pathlib import Path
import os
TIME_ZONE = 'Asia/Dhaka'
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']




# Application definition

INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sfbk',
    'corsheaders',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
]

AUTH_USER_MODEL = 'sfbk.UserAccount'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
from datetime import timedelta
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rajieb1618@gmail.com'
EMAIL_HOST_PASSWORD = 'uvzzspwpfwjolcxe'
EMAIL_USE_TLS = True

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid},{token}',
    'SERIALIZERS': {
        'user_create': 'sfbk.serializers.UserCreateSerializer',
        'user': 'sfbk.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'sfserver.urls'

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

WSGI_APPLICATION = 'sfserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static' / 'images'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:3000',
# )

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOWED_ORIGINS = [  
#     "http://localhost:3000",
# ]

# CORS_ALLOW_METHODS = (
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# )
# from corsheaders.defaults import default_headers

# CORS_ALLOW_HEADERS = default_headers + (
#     'Access-Control-Allow-Origin',
# )



######### UNFOLD SETTINGS #########

UNFOLD = {
    "SITE_TITLE": "Seatfinder",
    "SITE_HEADER": "SeatFinder",
    "SITE_URL": "/",
    "SITE_ICON": lambda request: static("icon.png"),
    "SITE_SYMBOL": "speed",  # symbol from icon set
    # "DASHBOARD_CALLBACK": "sfbk.dashboard_callback",
    "LOGIN": {
        "image": lambda r: static("mockup.png"),
        "redirect_after": lambda r: reverse_lazy("admin:sfbk_event_changelist"),
    },
    "STYLES": [
        lambda request: static("css/style.css"),
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),
    ],
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    # "SIDEBAR": {
    #     "show_search": False,  # Search in applications and models names
    #     "show_all_applications": False,  # Dropdown with all applications and models
    #     "navigation": [
    #         {
    #             "title": _("Navigation"),
    #             "separator": True,  # Top border
    #             "items": [
    #                 {
    #                     "title": _("Dashboard"),
    #                     "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
    #                     "link": reverse_lazy("admin:index"),
    #                     "badge": "sample_app.badge_callback",
    #                     "permission": lambda request: request.user.is_superuser,
    #                 },
    #                 {
    #                     "title": _("Users"),
    #                     "icon": "people",
    #                     # "link": reverse_lazy("admin:users_user_changelist"),
    #                 },
    #             ],
    #         },
    #     ],
    # },
    # "TABS": [
    #     {
    #         "models": [
    #             "sfbk.model_name_in_lowercase",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Your custom title"),
    #                 "link": reverse_lazy("admin:sfbk_label_model_name_changelist"),
    #                 # "permission": "sfbk.permission_callback",
    #             },
    #         ],
    #     },
    # ],
}


def dashboard_callback(request, context):
    """
    Callback to prepare custom variables for index template which is used as dashboard
    template. It can be overridden in application by creating custom admin/index.html.
    """
    context.update(
        {
            "sample": "example",  # this will be injected into templates/admin/index.html
        }
    )
    return context


def badge_callback(request):
    return 3

def permission_callback(request):
    return request.user.has_perm("sample_app.change_model")