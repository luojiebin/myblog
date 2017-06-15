from .base import *

DEBUG = False

ADMINS = (
    ('luojiebin', 'luo.jiebin@qq.com'),
)

ALLOWED_HOSTS = ['luojiebin.com', '47.92.121.144']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myblog',
        'USER': 'myblog',
        'PASSWORD': os.environ.get('MYBLOG_POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
