from django.urls import path

from clave_unica_auth import settings
from .views import claveunica_login, claveunica_callback

urlpatterns = [
    path(settings.get('CLAVEUNICA_PATH_LOGIN'), claveunica_login, name='clave_unica_auth_login'),
    path(settings.get('CLAVEUNICA_PATH_REDIRECT'), claveunica_callback, name='clave_unica_auth_callback'),
]
