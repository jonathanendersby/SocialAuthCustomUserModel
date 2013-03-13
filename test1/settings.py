DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test.db',                      # Or path to database file if using sqlite3.
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'y=#e$83y02stda*y&h$03$3a=8%kvf&gfi7m=e^gwnhxk#tyum'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'test1.urls'
WSGI_APPLICATION = 'test1.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'myapp',
    'social_auth',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL          = '/'
LOGIN_REDIRECT_URL = '/post'
LOGIN_ERROR_URL    = '/error'

GOOGLE_OAUTH2_CLIENT_ID = 'CLIENTIDCLIENTIDCLIENTIDCLIENTID'
GOOGLE_OAUTH2_CLIENT_SECRET = 'CLIENTSECRETCLIENTSECRETCLIENTSECRET'

AUTH_USER_MODEL = 'myapp.User'
SOCIAL_AUTH_USER_MODEL = 'myapp.User'
