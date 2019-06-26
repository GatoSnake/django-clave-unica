from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib.parse import urlencode

import requests
import json
import uuid

# Create your views here.
def redirect_to_clave_unica(request):
    """Redirect a clave unica"""
    state = uuid.uuid4()
    print(state)
    params = {
        "client_id": "",
        "response_type": "code",
        "scope": "openid run name email",
        "redirect_uri": "https://local.agilesigner.com/testclaveunica/callback",
        "state": state,
    }
    params = urlencode(params)
    print(params)
    url = f"https://accounts.claveunica.gob.cl/openid/authorize?{params}"
    print(url)
    return redirect(url)

def redirect_from_clave_unica(request):
    """Intercambio authorization_code a access_token y obtener info de usuario"""
    #TODO: PENDIENTE VERIFICACION STATE
    print(request.GET.get('state'))
    print(request.GET.get('code'))
    
    data = {
        "client_id": "",
        "client_secret": "",
        "redirect_uri": "https://local.agilesigner.com/testclaveunica/callback",
        "grant_type": "authorization_code",
        "code": request.GET.get("code"),
        "state": request.GET.get("state"),
    }

    url = "https://accounts.claveunica.gob.cl/openid/token/"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "User-Agent": "My User Agent 1.0"
    }
    resp = requests.post(url, data=data, headers=headers)
    print(resp.json())
    if resp.status_code != 200:
        return HttpResponse(f'Error code: {resp.status_code} en intercambio token')
  
    #obtener info usuario
    url = "https://accounts.claveunica.gob.cl/openid/userinfo/"
    headers = {
        "Authorization": f"Bearer {resp.json().get('access_token')}",
        "Accept": "application/json",
        "User-Agent": "My User Agent 1.0"
    }
    resp = requests.post(url, headers=headers)
    if resp.status_code != 200:
        return HttpResponse(f'Error code: {resp.status_code} en obtener info user')
    print(resp)

    return HttpResponse(resp)