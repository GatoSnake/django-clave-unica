# Django Clave Unica

Aplicación Djando que permite la autenticación de los ciudadanos de Chile.

[![GitHub release](https://img.shields.io/github/release/gatosnake/django-clave-unica.svg)](https://github.com/GatoSnake/django-clave-unica/releases/)
[![GitHub tag](https://img.shields.io/github/tag/gatosnake/django-clave-unica.svg)](https://github.com/GatoSnake/django-clave-unica/tags/)
[![GitHub license](https://img.shields.io/github/license/gatosnake/django-clave-unica.svg)](https://github.com/GatoSnake/django-clave-unica/blob/master/LICENSE)
[![Github all releases](https://img.shields.io/github/downloads/gatosnake/django-clave-unica/total.svg)](https://github.com/GatoSnake/django-clave-unica/releases/)

## Codigo Fuente

El código fuente de la aplicación lo puedes obtener de la siguiente url en Github:
https://github.com/GatoSnake/django-clave-unica

Si esta aplicación te fue de ayuda, no dudes en compartirlo y hacermelo saber. :blush: :beers:

Además, esta abierto para que hagan sus pull requests en casos de realizar mejoras al código. :sunglasses:

## Instalación

1. Descarga e instala el paquete utilizando `pipenv` o `pip` de la siguiente manera:
```
pip install django-clave-unica
```

2. Agrega la aplicación `clave_unica_auth` en el parámetro INSTALLED_APPS de tu archivo `settings.py`, 
de la siguiente manera:
```python
INSTALLED_APPS = [
	...
	'clave_unica_auth',
]
```

3. Incluir las credenciales de la aplicación para la autenticación de los usuarios. Como parámetros mínimos, debe ingresar en el archivo `settings.py` lo siguiente:
```python
CLAVE_UNICA = {
    'CLIENT_ID': 'client_id',
    'CLIENT_SECRET': 'client_secret',
    'REDIRECT_URI': 'redirect_uri',
}
```
**Para obtener tus credenciales de integración con Clave Única, accede a https://claveunica.gob.cl/institucional.**

4. Incluye la ruta de autenticación Clave Única en el archivo `urls.py` de tu proyecto, 
de la siguiente manera:
```python
urlpatterns = [
		...
	path('claveunica/', include('clave_unica_auth.urls')),
	...
]
```

5. Ejecutar `python manage.py migrate` para migrar el modelo de personas de Clave Unica a la base de datos.

6. Ejecutar el servidor de desarrollo y acceder a http://127.0.0.1:8000/claveunica/login para realizar el proceso de autenticación.

## Funcionamiento

1. Cuando un usuario iniciar sesión contra Clave Única, el sistema lo redirige al portal de autenticación creando para esa sesion de autenticación un parámetro llamado `state` en formato UUIDv4, en el cual dura 30 minutos y se guarda en el cache por defecto de Django. 
2. Si las credenciales del usuario son correctas, Clave Única redirige nuevamente al usuario a la aplicación a través de una URL callback que es registrada por el dueño de la aplicación en en registro de instituciones de clave Única (https://claveunica.gob.cl/institucional).
3. El sistema verifica el parametro `state`, si no ha expirado entonces verifica si el usuario existe en base de datos. En caso de no existir lo crea automaticamente y lo dirige a la vista ya autenticada.

A nivel de base de datos, la estructura de los datos esta compuesta de la siguiente manera:
* La columna `username` de la tabla de usuario de Django posee la información del RUN de la persona.
* La información de la persona, como el RUN y el DV esta guardada en la tabla `clave_unica_auth_person`, en el cual esta asociada a la tabla de usuarios de Django.
* La tabla `clave_unica_auth_login` posee el registro de todos los intentos de inicios de sesión. En ella se guarda la fecha, dirección IP remoto, el parámetro state, el resultado de la autenticación y el usuario asociado si este existe en BD.

## Otras configuraciones

### CLAVEUNICA_URL_LOGIN
Url de login en Clave Única.
```
Type: string
Default: https://accounts.claveunica.gob.cl/openid/authorize
```
### CLAVEUNICA_URL_LOGOUT
Url de logout Clave Única.
```
Type: string
Default: https://api.claveunica.gob.cl/api/v1/accounts/app/logout
```
### CLAVEUNICA_REMEMBER_LOGIN
Recuerda la autenticación del usuario de Clave Única.
```
Type: boolean
Default: False
```
NOTA: Para no recordar la autenticación del usuario, se realiza el truco de abrir un iframe escondido en el html con la url del parámetro `CLAVEUNICA_URL_LOGOUT`.
### CLAVEUNICA_TOKEN_URI
Url intercambio autorization_code a access_token en Clave Única.
```
Type: string
Default:  https://accounts.claveunica.gob.cl/openid/token
```
### CLAVEUNICA_USERINFO_URI
Url para obtención de información del usuario en Clave Única.
```
Type: string
Default:  https://accounts.claveunica.gob.cl/openid/userinfo
```
### CLAVEUNICA_STATE_TIMEOUT
Tiempo en segundos que dura el parámetro `state` antes de realizar la autenticación en Clave Única.
```
Type: int
Default:  1800
```
### CLAVEUNICA_AUTO_CREATE_USER
Crea automaticamente al usuario si no existe en BD.
```
Type: boolean
Default:  True
```
### CLAVEUNICA_PATH_LOGIN
Url path para login Clave Única.
```
Type: string
Default:  login/
```
### CLAVEUNICA_PATH_REDIRECT
Url path redirect desde Clave Única.
```
Type: string
Default:  callback/
```
### CLAVEUNICA_PATH_SUCCESS_LOGIN
Url path a vista que se redirige despues de hacer login correctamente.
```
Type: string
Default:  /home/
```
### CLAVEUNICA_HTML_ERROR
Path archivo error html.
```
Type: string
Default:  clave_unica_auth/error.html
```

## Changelog

* **1.0.1** [14/07/19]
	* Se cambia la configuracion Clave Única a tipo diccionario en settings.py.
* **1.0.0** [07/07/19]
	* Permite la autenticación de los usuarios via Clave Única.
