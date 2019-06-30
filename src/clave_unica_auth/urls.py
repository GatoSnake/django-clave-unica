from django.urls import path

from .views import redirect_to_clave_unica, redirect_from_clave_unica

urlpatterns = [
    path('', redirect_to_clave_unica, name='clave_unica_auth_redirect'),
    path('callback/', redirect_from_clave_unica, name='clave_unica_auth_callback'),
]
