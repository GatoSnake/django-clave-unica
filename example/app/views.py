from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from clave_unica_auth import settings as claveunica_settings

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    context = {}
    if not claveunica_settings.get('REMEMBER_LOGIN'):
        context = {'url_logout': claveunica_settings.get('URL_LOGOUT')}
    return render(request, 'home.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))