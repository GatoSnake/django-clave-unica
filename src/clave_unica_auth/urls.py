from django.urls import path

from .views import claveunica_index, claveunica_logout, claveunica_login, claveunica_callback

urlpatterns = [
    path('', claveunica_index, name='clave_unica_auth_index'),
    path('logout/', claveunica_logout, name='clave_unica_auth_logout'),
    path('login/', claveunica_login, name='clave_unica_auth_redirect'),
    path('callback/', claveunica_callback, name='clave_unica_auth_callback'),
]
