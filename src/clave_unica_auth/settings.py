from django.conf import settings

class ClaveUnicaSettings():
    
    @property
    def CLAVEUNICA_CLIENT_ID(self):
        """REQUIRED. Client ID Clave Unica"""
        return settings.CLAVEUNICA_CLIENT_ID
    
    @property
    def CLAVEUNICA_CLIENT_SECRET(self):
        """REQUIRED. Client secret Clave Unica"""
        return settings.CLAVEUNICA_CLIENT_SECRET

    @property
    def CLAVEUNICA_URL_LOGIN(self):
        """OPTIONAL. Login hacia Clave Unica"""
        return settings.CLAVEUNICA_URL_LOGIN if hasattr(settings, 'CLAVEUNICA_URL_LOGIN') else 'https://accounts.claveunica.gob.cl/openid/authorize'

    @property
    def CLAVEUNICA_REDIRECT_URI(self):
        """REQUIRED. Url redirect desde Clave Unica"""
        return settings.CLAVEUNICA_REDIRECT_URI
    
    @property
    def CLAVEUNICA_TOKEN_URI(self):
        """OPTIONAL. Url intercambio autorization_code a access_token en Clave Unica"""
        return settings.CLAVEUNICA_TOKEN_URI if hasattr(settings, 'CLAVEUNICA_TOKEN_URI') else 'https://accounts.claveunica.gob.cl/openid/token'

    @property
    def CLAVEUNICA_USERINFO_URI(self):
        """OPTIONAL. Url para obtencion de informacion del usuario en Clave Unica"""
        return settings.CLAVEUNICA_USERINFO_URI if hasattr(settings, 'CLAVEUNICA_USERINFO_URI') else 'https://accounts.claveunica.gob.cl/openid/userinfo'

    @property
    def CLAVEUNICA_STATE_TIMEOUT(self):
        """OPTIONAL. Tiempo que dura el cache que guarda el parametro STATE antes de que expire en la autenticacion. Por defecto: 30 min"""
        return settings.CLAVEUNICA_STATE_TIMEOUT if hasattr(settings, 'CLAVEUNICA_STATE_TIMEOUT') else (60 * 30)
    
    @property
    def CLAVEUNICA_AUTO_CREATE_USER(self):
        """OPTIONAL. Crea automaticamente al usuario en BD. Defeault: true"""
        return settings.CLAVEUNICA_AUTO_CREATE_USER if hasattr(settings, 'CLAVEUNICA_AUTO_CREATE_USER') else True
    
claveunica_settings = ClaveUnicaSettings()

def get(name):
    try:
        return getattr(claveunica_settings, name)
    except AttributeError:
        raise Exception('You must set {name_setting} in your settings.'.format(name_setting=name))
