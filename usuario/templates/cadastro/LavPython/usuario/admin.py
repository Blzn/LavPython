from django.contrib import admin
from LavPython.usuario.models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')
    search_fields = ('nome','sobrenome')

admin.site.register(Usuario, UsuarioAdmin)
