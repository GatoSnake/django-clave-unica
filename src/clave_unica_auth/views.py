from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.cache import cache

from urllib.parse import urlencode

from .lib.utils import oauth2_claveunica
from .models import ClaveUnicaLogin
from clave_unica_auth import settings

# Create your views here.
def redirect_to_clave_unica(request):
    """Redirect a clave unica"""
    state = oauth2_claveunica.generate_state()
    cache.set(state, { 'remote_addr': request.META.get('REMOTE_ADDR') }, settings.get('CLAVEUNICA_TIMEOUT_CACHE'))
    return redirect(oauth2_claveunica.get_url_login_claveunica(settings.get('CLAVEUNICA_URL_LOGIN'), settings.get('CLAVEUNICA_CLIENT_ID'), settings.get('CLAVEUNICA_REDIRECT_URI'), state))

def redirect_from_clave_unica(request):
    """Intercambio authorization_code a access_token y obtener info de usuario"""
    state = request.GET.get('state')
    code = request.GET.get('code')
    cache_data = cache.get(state)
    # verificando state en cache, si existe entonces no ha expirado el state
    if cache_data is None:
        return HttpResponse('State expired')
    #cache.delete(state)
    #crea instancia ClaveUnicaLogin
    claveUnicaLogin = ClaveUnicaLogin()
    claveUnicaLogin.state = state
    claveUnicaLogin.authorization_code = code
    claveUnicaLogin.remote_addr = cache_data.get('remote_addr')
    try:
        #obtener authorization_code
        access_token_json = oauth2_claveunica.request_authorization_code(
            settings.get('CLAVEUNICA_TOKEN_URI'),
            settings.get('CLAVEUNICA_CLIENT_ID'),
            settings.get('CLAVEUNICA_CLIENT_SECRET'),
            settings.get('CLAVEUNICA_REDIRECT_URI'),
            claveUnicaLogin.authorization_code,
            claveUnicaLogin.state
        )
        claveUnicaLogin.access_token = access_token_json.get('access_token')
        #obtener info usuario
        info_user_json = oauth2_claveunica.request_info_user(
            settings.get('CLAVEUNICA_USERINFO_URI'),
            claveUnicaLogin.access_token
        )
        claveUnicaLogin.save()
        return HttpResponse(info_user_json)
    except Exception as e:
        claveUnicaLogin.save()
        return HttpResponse(e)
