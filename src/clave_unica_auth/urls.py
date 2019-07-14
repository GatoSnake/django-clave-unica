from django.urls import path

from clave_unica_auth import settings as claveunica_settings
from .views import claveunica_login, claveunica_callback

urlpatterns = [
    path(claveunica_settings.get('PATH_LOGIN'), claveunica_login, name='clave_unica_auth-login'),
    path(claveunica_settings.get('PATH_REDIRECT'), claveunica_callback, name='clave_unica_auth-callback'),
]
