from django.contrib import admin
from LavPython.trajeto.models import Trajeto,Coordenadas,Dia

class TrajetoAdmin(admin.ModelAdmin):
    list_display = ('nome','distancia',)
    search_fields = ('nome',)

class CoordenadasAdmin(admin.ModelAdmin):
    list_display = ('latitude','longitude',)

class DiaAdmin(admin.ModelAdmin):
    list_display = ('data','tipo','carro')
    search_fields = ('data',)

admin.site.register(Trajeto, TrajetoAdmin)
admin.site.register(Coordenadas, CoordenadasAdmin)
admin.site.register(Dia,DiaAdmin)
