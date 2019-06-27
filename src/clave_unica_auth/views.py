from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from urllib.parse import urlencode

from .models import ClaveUnicaLogin

import requests
import json
import uuid

# Create your views here.
def redirect_to_clave_unica(request):
    """Redirect a clave unica"""
    state = uuid.uuid4()
    cache_data = {
        'remote_addr': request.META.get('REMOTE_ADDR')
    }
    cache.set(state, cache_data, 2)
    params = {
        'client_id': '[CLIENT_ID]',
        'response_type': 'code',
        'scope': 'openid run name email',
        'redirect_uri': 'https://local.agilesigner.com/testclaveunica/callback',
        'state': state,
    }
    params = urlencode(params)
    url = 'https://accounts.claveunica.gob.cl/openid/authorize?{params}'.format(params=params)
    return redirect(url)

def redirect_from_clave_unica(request):
    """Intercambio authorization_code a access_token y obtener info de usuario"""
    state = request.GET.get('state')
    code = request.GET.get('code')
    cache_data = cache.get(state)
    #verificando state
    if cache_data is None:
        return HttpResponse('State expired')
    cache.delete(state)

    cuLogin = ClaveUnicaLogin()
    cuLogin.state = state
    cuLogin.authorization_code = code
    cuLogin.remote_addr = cache_data.get('remote_addr')
    cuLogin.save()

    data = {
        'client_id': '[CLIENT_ID]',
        'client_secret': '[CLIENT_SECRET]',
        'redirect_uri': 'https://local.agilesigner.com/testclaveunica/callback',
        'grant_type': 'authorization_code',
        'code': code,
        'state': state,
    }
    url = 'https://accounts.claveunica.gob.cl/openid/token/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'User-Agent': 'My User Agent 1.0'
    }
    resp = requests.post(url, data=data, headers=headers)
    if resp.status_code != 200:
        return HttpResponse('Error code: {status} en intercambio token'.format(status=resp.status_code))

    access_token = resp.json().get('access_token')
    cuLogin.access_token = access_token
    cuLogin.save()

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
