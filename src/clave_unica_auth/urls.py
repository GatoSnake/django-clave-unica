from django.urls import path

from .views import redirect_to_clave_unica, redirect_from_clave_unica

urlpatterns = [
    path('', redirect_to_clave_unica),
    path('callback/', redirect_from_clave_unica),
]
