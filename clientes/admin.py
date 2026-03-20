from django.contrib import admin
from .models import Cliente

# Register your models here.

# admin.site.register(Cliente)


@admin.register(Cliente)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'correo', 'telefono', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo', 'fecha_creacion')