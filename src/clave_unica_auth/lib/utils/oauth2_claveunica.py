from urllib.parse import urlencode

import uuid
import requests
import json

def generate_state():
    """genera un random UUIDv4 para el parametro state"""
    return uuid.uuid4()

def encode_dict_to_uri(params):
    """encodea un diccionario a formato URI"""
    return urlencode(params)

def join_url_with_params(url, params):
    """genera la url de redireccion a clave unica"""
    return '{url}?{params}'.format(url=url, params=params)

def get_url_params_authorization_code(client_id, redirect_uri, state=uuid.uuid4()):
    """obtiene los parametros encodeado en url que seran enviados para solicitar el authorization_code Clave Unica"""
    return encode_dict_to_uri({
        'client_id': client_id,
        'response_type': 'code',
        'scope': 'openid run name email',
        'redirect_uri': redirect_uri,
        'state': state,
    })

def get_params_access_token(client_id, client_secret, redirect_uri, code, state=uuid.uuid4()):
    """obtiene los parametros encodeado en url que seran enviados para solicitar el access_token Clave Unica"""
    return {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
        'code': code,
        'state': state,
    }

def get_headers_authorization_code():
    return {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'User-Agent': 'My User Agent 1.0'
    }

def get_url_login_claveunica(url, client_id, redirect_uri, state=uuid.uuid4()):
    """obtiene la url que redirige a clave unica para login"""
    print(get_url_params_authorization_code(client_id, redirect_uri, state))
    return join_url_with_params(url, get_url_params_authorization_code(client_id, redirect_uri, state))

def request_authorization_code(url, client_id, client_secret, redirect_uri, code, state=uuid.uuid4()):
    """solicitud POST authorization_code a Clave Unica"""
    print('HACIENDO REQUEST POST!')
    resp = requests.post(url, data=get_params_access_token(), headers=get_headers_authorization_code())
    print(resp.status_code)
    if resp.status_code != 200:
        raise Exception('Error code: {status_code} en intercambio token'.format(status_code=resp.status_code))
    return resp.json()
    