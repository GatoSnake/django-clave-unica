from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Login, Person

admin.site.unregister(User)

class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'Person'

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (PersonInline,)

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('login_date', 'remote_addr', 'user', 'completed')
    list_filter = ('login_date', 'completed')
    search_fields = ['state', 'remote_addr', 'user__username', 'user__first_name', 'user__last_name']
    readonly_fields = ('state', 'authorization_code', 'login_date', 'remote_addr', 'access_token', 'completed', 'user')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
