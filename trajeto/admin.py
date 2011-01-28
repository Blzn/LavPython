from django.contrib import admin
from LavPython.trajeto.models import Trajeto,Coordenadas

class TrajetoAdmin(admin.ModelAdmin):
    list_display = ('nome','distancia',)
    search_fields = ('nome',)

class CoordenadasAdmin(admin.ModelAdmin):
    list_display = ('latitude','longitude',)


admin.site.register(Trajeto, TrajetoAdmin)
admin.site.register(Coordenadas, CoordenadasAdmin)
