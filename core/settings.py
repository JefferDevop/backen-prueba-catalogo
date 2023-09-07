from pathlib import Path
import datetime
import os

import cloudinary
import cloudinary.uploader
import cloudinary.api



BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!fr6a*b!3hydo5@#j#ycc6(&5f4xd_$3z=(ws%jm3*!e2!nm!&'

DEBUG = True

ALLOWED_HOSTS = ["*"]

 
SHARED_APPS = (
    'django_tenants',    
    'customers',
    # "admin_interface",
    'django.contrib.contenttypes',
)

TENANT_APPS = (   
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',    
    'rest_framework',
    'simple_history',
    'cloudinary',    
    'drf_yasg',
    'corsheaders',    
    'colorfield',    
    'django_filters',
    'accounts',
    'products',
    'carts',
    'warehome',
    'stores',
    'company',
)

INSTALLED_APPS = list(SHARED_APPS) + \
    [app for app in TENANT_APPS if app not in SHARED_APPS]



MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ]


    

SESSION_EXPIRE_SECONDS = 1800  # 1/2 hour
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'accounts/login'

ROOT_URLCONF = 'core.urls'

X_FRAME_OPTIONS = "SAMEORIGIN"


TENANT_MODEL = "customers.Client"
TENANT_DOMAIN_MODEL = "customers.Domain"

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)



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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


##Local
#
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'archivoplano',
        'USER': 'SYSDBA',
        'PASSWORD': 'D3s4rr0ll0',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


##Prueba
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_tenants.postgresql_backend',
#         # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': '2yM5cNtLuIELNsuXSxar',
#         'HOST': 'containers-us-west-71.railway.app',
#         'PORT': '6061',
#     }
# }

##Produccion
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_tenants.postgresql_backend',
#         # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'gkESA9gdKSJH7OV9rPBQ',
#         'HOST': 'containers-us-west-109.railway.app',
#         'PORT': '7067',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

cloudinary.config(
    cloud_name="dnio5vufj",
    api_key="539833493919715",
    api_secret="huxBbY9u3457XMDHBUqihOntga8",
    #   secure = true
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.Account'

CORS_ORIGIN_ALLOW_ALL = True
CARS_ALLOW_CREDENCIALS = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=100)
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# print(MEDIA_ROOT)
# Tenant Config
