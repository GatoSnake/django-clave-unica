from django.db import models
from django.core.cache import cache

import uuid
import requests
import json

# Create your models here.
class ClaveUnicaLogin(models.Model):
    state = models.UUIDField(default=uuid.uuid4)
    login_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    authorization_code = models.CharField(max_length=120)
    access_token = models.CharField(max_length=120)
    remote_addr = models.CharField(max_length=254, null=True)

    class Meta:
        verbose_name_plural ='Clave Unica Login'

    def __str__(self):
        return str(self.state)
    
    
    def save_in_cache(self, key, data, timeout=60 * 5):
        """guarda dato en cache"""
        cache.set(key, data, timeout)
