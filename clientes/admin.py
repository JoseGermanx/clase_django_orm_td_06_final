from django.contrib import admin
from .models import Cliente
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'edad', 'telefono', 'activo', 'fecha_creacion')
    search_fields = ('nombre', 'apellido', 'correo')
    list_filter = ('activo', 'fecha_creacion')


class UserAdminPersonalizado(UserAdmin):
    list_display = ('username', 'email')
    search_fields = ('email',)
    list_filter = ("is_staff",)

admin.site.unregister(User)
admin.site.register(User, UserAdminPersonalizado)

# admin.site.register(Cliente, ClienteAdmin)