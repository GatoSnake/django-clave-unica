from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('clave_unica_index'))