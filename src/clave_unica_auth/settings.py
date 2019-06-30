from django.conf import settings

class ClaveUnicaSettings():
    
    @property
    def CLAVEUNICA_CLIENT_ID(self):
        """REQUIRED.\n
        Client ID Clave Unica
        """
        return settings.CLAVEUNICA_CLIENT_ID
    
    @property
    def CLAVEUNICA_CLIENT_SECRET(self):
        """REQUIRED.\n
        Client secret Clave Unica
        """
        return settings.CLAVEUNICA_CLIENT_SECRET

    @property
    def CLAVEUNICA_URL_LOGIN(self):
        """OPTIONAL.\n
        Login hacia Clave Unica
        """
        return settings.CLAVEUNICA_URL_LOGIN if hasattr(settings, 'CLAVEUNICA_URL_LOGIN') else 'https://accounts.claveunica.gob.cl/openid/authorize'

    @property
    def CLAVEUNICA_REDIRECT_URI(self):
        """REQUIRED.\n
        Url redirect desde Clave Unica
        """
        return settings.CLAVEUNICA_REDIRECT_URI
    
    @property
    def CLAVEUNICA_TOKEN_URI(self):
        """OPTIONAL\n
        DEFAULT: https://accounts.claveunica.gob.cl/openid/token\n
        Url intercambio autorization_code a access_token en Clave Unica.
        """
        return settings.CLAVEUNICA_TOKEN_URI if hasattr(settings, 'CLAVEUNICA_TOKEN_URI') else 'https://accounts.claveunica.gob.cl/openid/token'

    @property
    def CLAVEUNICA_USERINFO_URI(self):
        """OPTIONAL.\n
        DEFAULT: https://accounts.claveunica.gob.cl/openid/userinfo\n
        Url para obtencion de informacion del usuario en Clave Unica.
        """
        return settings.CLAVEUNICA_USERINFO_URI if hasattr(settings, 'CLAVEUNICA_USERINFO_URI') else 'https://accounts.claveunica.gob.cl/openid/userinfo'

    @property
    def CLAVEUNICA_STATE_TIMEOUT(self):
        """OPTIONAL.\n
        DEFAULT: 30 min\n
        Tiempo que dura el parametro State antes de realizar la autenticacion en Clave Unica.
        """
        return settings.CLAVEUNICA_STATE_TIMEOUT if hasattr(settings, 'CLAVEUNICA_STATE_TIMEOUT') else (60 * 30)
    
    @property
    def CLAVEUNICA_AUTO_CREATE_USER(self):
        """OPTIONAL.\n
        DEFAULT: False\n
        Crea automaticamente al usuario si no existe en BD.
        """
        return settings.CLAVEUNICA_AUTO_CREATE_USER if hasattr(settings, 'CLAVEUNICA_AUTO_CREATE_USER') else False
    
claveunica_settings = ClaveUnicaSettings()

def get(name):
    try:
        return getattr(claveunica_settings, name)
    except AttributeError:
        raise Exception('You must set {name_setting} in your settings.'.format(name_setting=name))
