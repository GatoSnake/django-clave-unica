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
    cache.delete(state)

    cuLogin = ClaveUnicaLogin()
    cuLogin.state = state
    cuLogin.authorization_code = code
    cuLogin.remote_addr = cache_data.get('remote_addr')


    # access_token = resp.json().get('access_token')
    # cuLogin.access_token = access_token
    # cuLogin.save()

    try:
        access_token_json = oauth2_claveunica.request_authorization_code(
            settings.get('CLAVEUNICA_TOKEN_URI'),
            settings.get('CLAVEUNICA_CLIENT_ID'),
            settings.get('CLAVEUNICA_CLIENT_SECRET'),
            settings.get('CLAVEUNICA_REDIRECT_URI'),
            code,
            state
        )
    except Exception as e:
        return HttpResponse(e.__cause__)

    #obtener info usuario
    url = 'https://accounts.claveunica.gob.cl/openid/userinfo/'
    headers = {
        'Authorization': 'Bearer {access_token}'.format(access_token=access_token),
        'Accept': 'application/json',
        'User-Agent': 'My User Agent 1.0'
    }
    resp = requests.post(url, headers=headers)
    if resp.status_code != 200:
        return HttpResponse('Error code: {status} en obtener info user'.format(status=resp.status_code))
    print(resp)

    return HttpResponse(resp)
