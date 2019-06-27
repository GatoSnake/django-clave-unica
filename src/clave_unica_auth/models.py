from django.db import models

import uuid

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
        
