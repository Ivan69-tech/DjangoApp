from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = 'twj_&nv69tt79_mfs)hn@5uo+(+b@#kp#uk&8lxt$a=86*m26%'

ALLOWED_HOSTS = ["le-site-de-ivan.herokuapp.com"]

MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

SECURE_SSL_REDIRECT = True # [1]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        "symmetric_encryption_keys": [SECRET_KEY],
    },
}