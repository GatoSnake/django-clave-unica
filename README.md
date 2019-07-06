# Django Clave Unica

Aplicacion Djando que permite la autenticacion de los ciudadanos de Chile.

## Instalacion

1. Agrega la aplicacion `clave_unica_auth` en el parametro INSTALLED_APPS de tu archivo `settings.py`, 
de la siguiente manera:\
```python
INSTALLED_APPS = [
		...
		'clave_unica_auth',
]
```
2. Incluir las credenciales de la aplicacion para la autenticacion OpenID de los usuarios. Como parametros minimos, debe ingresar en el archivo `settings.py` lo siguiente:
```python
CLAVEUNICA_CLIENT_ID = 'client_id'
CLAVEUNICA_CLIENT_SECRET = 'client_secret'
CLAVEUNICA_REDIRECT_URI = 'redirect_uri'
```
**Para obtener tus credenciales de integracion, accede a https://claveunica.gob.cl/institucional.
**
3. Incluye la autenticacion Clave Unica en el archivo urls.py de tu proyecto, 
de la siguiente manera:
```python
urlpatterns = [
		...
		path('claveunica/', include('clave_unica_auth.urls')),
		...
]
```

4. Ejecutar `python manage.py migrate` para migrar el modelo de personas de Clave Unica a la base de datos.

5. Ejecutar el servidor de desarrollo y acceder a http://127.0.0.1:8000/claveunica/login para realizar el proceso de autenticacion.

## Otras opciones

### CLAVEUNICA_URL_LOGIN
Url de login en Clave Unica.
**Type:** string
**Default:** https://accounts.claveunica.gob.cl/openid/authorize
### CLAVEUNICA_URL_LOGOUT
Url de logout Clave Unica.
**Type:** string
**Default:** https://api.claveunica.gob.cl/api/v1/accounts/app/logout
### CLAVEUNICA_REMEMBER_LOGIN
Recuerda la autenticacion del usuario de Clave Unica. 
**Type:** boolean
**Default:** True
NOTA: Para no recordar la autenticacion del usuario, se realiza el truco de abrir un iframe escondido en el html con la url del parametro `CLAVEUNICA_URL_LOGOUT`.
### CLAVEUNICA_TOKEN_URI
Url intercambio autorization_code a access_token en Clave Unica.
**Type:** string
**Default:**  https://accounts.claveunica.gob.cl/openid/token
### CLAVEUNICA_USERINFO_URI
Url para obtencion de informacion del usuario en Clave Unica.
**Type:** string
**Default:**  https://accounts.claveunica.gob.cl/openid/userinfo
### CLAVEUNICA_STATE_TIMEOUT
Tiempo en segundos que dura el parametro `state` antes de realizar la autenticacion en Clave Unica.
**Type:** int
**Default:**  1800
### CLAVEUNICA_AUTO_CREATE_USER
Crea automaticamente al usuario si no existe en BD.
**Type:** boolean
**Default:**  False
### CLAVEUNICA_PATH_LOGIN
Url path para login Clave Unica.
**Type:** string
**Default:**  login/
### CLAVEUNICA_PATH_REDIRECT
Url path redirect desde Clave Unica.
**Type:** string
**Default:**  callback/
### CLAVEUNICA_PATH_SUCCESS_LOGIN
Url path a vista que se redirige despues de hacer login correctamente.
**Type:** string
**Default:**  /home/
### CLAVEUNICA_HTML_ERROR
Path archivo error html
**Type:** string
**Default:**  clave_unica_auth/error.html
