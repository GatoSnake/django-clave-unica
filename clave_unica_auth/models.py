from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User

import uuid

class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.UUIDField(default=uuid.uuid4)
    login_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    authorization_code = models.CharField(max_length=120)
    access_token = models.CharField(max_length=120)
    remote_addr = models.CharField(max_length=254, null=True)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural ='Login'

    def __str__(self):
        return str(self.state) + ' | ' +  str(self.login_date) + (' | ' + str(self.user) if self.user is not None else '')

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    run_type = models.CharField(max_length=50)
    run_num = models.IntegerField()
    run_dv = models.CharField(max_length=1)
    
    def __str__(self):
        return str(str(self.run_num) + '-' + self.run_dv)
    
    def parse_json(self, info_user_json):
        """parsea json a datos del modelo PersonClaveUnica"""
        self.run_type = info_user_json['RolUnico']['tipo']
        self.run_num = info_user_json['RolUnico']['numero']
        self.run_dv = info_user_json['RolUnico']['DV']
    
    def parse_json_to_user(self, info_user_json):
        """parsea un json y retorna una instancia nueva de User"""
        run = info_user_json['RolUnico']['numero']
        dv = info_user_json['RolUnico']['DV']
        email = info_user_json['email']
        runWithDV = str(run) + '-' + str(dv)
        first_name = ' '.join(info_user_json['name']['nombres'])
        last_name = ' '.join(info_user_json['name']['apellidos'])
        #setting data user
        user = User()
        user.username = runWithDV
        user.first_name = first_name
        user.email = email
        user.last_name = last_name
        return user
    