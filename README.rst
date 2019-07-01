=====
Clave Unica Authentication
=====

Aplicacion Djando que permite la autenticacion de los ciudadanos de Chile.

Quick start
-----------

1. Agregar "clave_unica_auth" en el parametro INSTALLED_APPS de tu archivo settings.py, 
de la siguiente manera::

    INSTALLED_APPS = [
        ...
        'clave_unica_auth',
    ]

2. Incluir las credenciales de la aplicacion para la autenticacion OpenID de los usuarios. 
Como parametros minimos, debe ingresar en el archivo settings.py lo siguiente:

    CLAVEUNICA_CLIENT_ID = 'client_id'
    CLAVEUNICA_CLIENT_SECRET = 'client_secret'
    CLAVEUNICA_REDIRECT_URI = 'redirect_uri'

Para obtener tus credenciales de integracion, accede a https://claveunica.gob.cl/institucional.

3. Incluye la autenticacion Clave Unica en el archivo urls.py de tu proyecto, 
de la siguiente manera::

    path('claveunica/', include('clave_unica_auth.urls')),

4. Ejecutar `python manage.py migrate` para crear el modelo de personas Clave Unica.

5. Ejecutar el servidor de desarrollo y acceder a  http://127.0.0.1:8000/claveunica/
   para realizar el proceso de autenticacion.
