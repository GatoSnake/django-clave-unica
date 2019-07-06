from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from clave_unica_auth import settings as cu_settings

def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    context = {}
    if not cu_settings.get('CLAVEUNICA_REMEMBER_LOGIN'):
        context = {'url_logout': cu_settings.get('CLAVEUNICA_URL_LOGOUT')}
    return render(request, 'home.html', context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))