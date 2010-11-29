from django.contrib import admin
from LavPython.usuario.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')

admin.site.register(Usuario, UsuarioAdmin)
