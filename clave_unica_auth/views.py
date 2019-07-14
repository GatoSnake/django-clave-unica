from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib.auth.models import User
from django.contrib.auth import login

from .lib.utils import oauth2_claveunica
from .models import Login as LoginClaveUnica, Person as PersonClaveUnica
from clave_unica_auth import settings as claveunica_settings

def claveunica_login(request):
    """Redirect a Clave Unica"""
    state = oauth2_claveunica.generate_state()
    cache.set(state, { 'remote_addr': request.META.get('REMOTE_ADDR') }, claveunica_settings.get('STATE_TIMEOUT'))
    return redirect(oauth2_claveunica.get_url_login_claveunica(claveunica_settings.get('URL_LOGIN'), claveunica_settings.get('CLIENT_ID'), claveunica_settings.get('REDIRECT_URI'), state))

def claveunica_callback(request):
    """Intercambio authorization_code a access_token y obtener info de usuario"""
    state = request.GET.get('state')
    code = request.GET.get('code')
    cache_data = cache.get(state)
    # verificando state en cache, si existe entonces no ha expirado el state
    if cache_data is None:
        context = {
            'error': 'State expirado',
            'description': 'El parametro state ha expirado. Por favor, vuelva a iniciar sesion.',
        }
        return claveunica_error(request, context)
    cache.delete(state)
    #crea instancia loginClaveUnica
    loginClaveUnica = LoginClaveUnica()
    loginClaveUnica.state = state
    loginClaveUnica.authorization_code = code
    loginClaveUnica.remote_addr = cache_data.get('remote_addr')
    clientSecret = claveunica_settings.get('CLIENT_SECRET')
    try:
        #obtener authorization_code
        access_token_json = oauth2_claveunica.request_authorization_code(
            claveunica_settings.get('TOKEN_URI'),
            claveunica_settings.get('CLIENT_ID'),
            clientSecret,
            claveunica_settings.get('REDIRECT_URI'),
            loginClaveUnica.authorization_code,
            loginClaveUnica.state
        )
        loginClaveUnica.access_token = access_token_json.get('access_token')
        #obtener info usuario
        info_user_json = oauth2_claveunica.request_info_user(
            claveunica_settings.get('USERINFO_URI'),
            loginClaveUnica.access_token
        )
    except Exception as e:
        #se guarda el login clave unica en bd a pesar de sea error, para guardar evidencia de auth
        loginClaveUnica.save()
        context = {
            'error': e.message if hasattr(e, 'message') else 'Error en Clave Unica',
            'description': e,
        }
        return claveunica_error(request, context)
    try:
        username = str(info_user_json['RolUnico']['numero'])+'-'+str(info_user_json['RolUnico']['DV'])
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        if claveunica_settings.get('AUTO_CREATE_USER'):
            #crea usuario y person en bd
            personClaveUnica = PersonClaveUnica()
            personClaveUnica.parse_json(info_user_json)
            user = personClaveUnica.parse_json_to_user(info_user_json)
            user.save()
            personClaveUnica.user = user
            personClaveUnica.save()
        else:
            loginClaveUnica.save()
            context = {
                'error': 'Usuario no registrado',
                'description': 'El usuario no se encuentra actualmente registrado.',
            }
            return claveunica_error(request, context)
    if user is not None:
        login(request, user)
        loginClaveUnica.user = user
        loginClaveUnica.completed = True
        loginClaveUnica.save()
        return redirect(claveunica_settings.get('PATH_SUCCESS_LOGIN'))
    else:
        loginClaveUnica.save()
        context = {
            'error': 'Error en autenticacion',
            'description': 'No se ha logrado autenticar el usuario.',
        }
        return claveunica_error(request, context)

def claveunica_error(request, context={'error': 'Error autenticación', 'description': 'Error en autenticación del usuario.'}):
    """Error vista clave unica"""
    if not claveunica_settings.get('REMEMBER_LOGIN'):
        context['url_logout'] = claveunica_settings.get('URL_LOGOUT')
    return render(request, claveunica_settings.get('HTML_ERROR'), context)