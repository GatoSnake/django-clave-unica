from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import LoginClaveUnica, PersonClaveUnica

# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PersonClaveUnicaInline(admin.StackedInline):
    model = PersonClaveUnica
    can_delete = False
    verbose_name_plural = 'person'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PersonClaveUnicaInline,)

class LoginClaveUnicaAdmin(admin.ModelAdmin):
    list_display = ('login_date', 'remote_addr', 'user', 'completed')
    readonly_fields = ('state', 'authorization_code', 'login_date', 'remote_addr', 'access_token', 'completed', 'user')


admin.site.register(LoginClaveUnica, LoginClaveUnicaAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
