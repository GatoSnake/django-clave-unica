from django.conf import settings

class ClaveUnicaSettings():
    
    @property
    def CLIENT_ID(self):
        """REQUIRED.\n
        Client ID Clave Unica
        """
        return settings.CLAVE_UNICA['CLIENT_ID']
    
    @property
    def CLIENT_SECRET(self):
        """REQUIRED.\n
        Client secret Clave Unica
        """
        return settings.CLAVE_UNICA['CLIENT_SECRET']

    @property
    def URL_LOGIN(self):
        """OPTIONAL.\n
        DEFAULT: https://accounts.claveunica.gob.cl/openid/authorize\n
        Login hacia Clave Unica
        """
        return settings.CLAVE_UNICA['URL_LOGIN'] if checkSetting('URL_LOGIN') else 'https://accounts.claveunica.gob.cl/openid/authorize'

    @property
    def URL_LOGOUT(self):
        """OPTIONAL.\n
        DEFAULT: https://api.claveunica.gob.cl/api/v1/accounts/app/logout\n
        Logout de Clave Unica. Esto se ejecuta en el navegador del cliente para borrar cookies de Clave Unica.
        """
        return settings.CLAVE_UNICA['URL_LOGOUT'] if checkSetting('URL_LOGOUT') else 'https://api.claveunica.gob.cl/api/v1/accounts/app/logout'

    @property
    def REMEMBER_LOGIN(self):
        """OPTIONAL.\n
        DEFAULT: False\n
        Recuerda la autenticacion del usuario de Clave Unica. En caso de siempre solicitar las credenciales de clave unica, setear False
        """
        return settings.CLAVE_UNICA['REMEMBER_LOGIN'] if checkSetting('REMEMBER_LOGIN') else False

    @property
    def REDIRECT_URI(self):
        """REQUIRED.\n
        Url redirect desde Clave Unica
        """
        return settings.CLAVE_UNICA['REDIRECT_URI']
    
    @property
    def TOKEN_URI(self):
        """OPTIONAL\n
        DEFAULT: https://accounts.claveunica.gob.cl/openid/token\n
        Url intercambio autorization_code a access_token en Clave Unica.
        """
        return settings.CLAVE_UNICA['TOKEN_URI'] if checkSetting('TOKEN_URI') else 'https://accounts.claveunica.gob.cl/openid/token'

    @property
    def USERINFO_URI(self):
        """OPTIONAL.\n
        DEFAULT: https://accounts.claveunica.gob.cl/openid/userinfo\n
        Url para obtencion de informacion del usuario en Clave Unica.
        """
        return settings.CLAVE_UNICA['USERINFO_URI'] if checkSetting('USERINFO_URI') else 'https://accounts.claveunica.gob.cl/openid/userinfo'

    @property
    def STATE_TIMEOUT(self):
        """OPTIONAL.\n
        DEFAULT: 30 min\n
        Tiempo que dura el parametro State antes de realizar la autenticacion en Clave Unica.
        """
        return settings.CLAVE_UNICA['STATE_TIMEOUT'] if checkSetting('STATE_TIMEOUT') else (60 * 30)
    
    @property
    def AUTO_CREATE_USER(self):
        """OPTIONAL.\n
        DEFAULT: True\n
        Crea automaticamente al usuario si no existe en BD.
        """
        return settings.CLAVE_UNICA['AUTO_CREATE_USER'] if checkSetting('AUTO_CREATE_USER') else True

    @property
    def PATH_LOGIN(self):
        """OPTIONAL.\n
        DEFAULT: login/\n
        Path interno a vista de login
        """
        return settings.CLAVE_UNICA['PATH_LOGIN'] if checkSetting('PATH_LOGIN') else 'login/'

    @property
    def PATH_REDIRECT(self):
        """OPTIONAL.\n
        DEFAULT: callback/\n
        Path url interna redirect desde Clave Unica
        """
        return settings.CLAVE_UNICA['PATH_REDIRECT'] if checkSetting('PATH_REDIRECT') else 'callback/'

    @property
    def PATH_SUCCESS_LOGIN(self):
        """OPTIONAL.\n
        DEFAULT: /home/\n
        Path url interna a la vista cuando el inicio se realiza correctamente
        """
        if checkSetting('PATH_SUCCESS_LOGIN'):
            if not settings.CLAVE_UNICA['PATH_SUCCESS_LOGIN']:
                return '/'
            return settings.CLAVE_UNICA['PATH_SUCCESS_LOGIN']
        else:
            return '/home/'

    @property
    def HTML_ERROR(self):
        """OPTIONAL.\n
        DEFAULT: clave_unica_auth/error.html\n
        Path html error
        """
        return settings.CLAVE_UNICA['HTML_ERROR'] if checkSetting('HTML_ERROR') else 'clave_unica_auth/error.html'

claveunica_settings = ClaveUnicaSettings()

def checkSetting(key):
    return hasattr(settings, 'CLAVE_UNICA') and key in settings.CLAVE_UNICA

def get(name):
    try:
        return getattr(claveunica_settings, name)
    except KeyError:
        raise Exception('You must set CLAVEUNICA[\'{name_setting}\'] in your settings.'.format(name_setting=name))
