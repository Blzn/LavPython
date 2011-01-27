from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline

from models import Marca, Carro, Fabricante, Motor, PastilhaFreio, CarroUsuario

class AdminMarca(admin.ModelAdmin):
	list_display = ('nome',)

class AdminCarro(admin.ModelAdmin):
	list_display = ('marca', 'modelo')
	search_fields = ('marca',)
	list_filter = ('marca',)

class AdminFabricante(admin.ModelAdmin):
	list_display  = ('nome',)
	search_fields = ('nome',)
	ordering = ('nome',)
	
class AdminMotor(admin.ModelAdmin):
	list_display = ('fabricante','modelo')
	search_fields = ('combustivel','potencia','modelo')
	list_filter = ('carros', 'fabricante')
	ordering = ('fabricante',)

class AdminPastilha(admin.ModelAdmin):
	list_display = ('fabricante','modelo')
	search_fields = ('modelo',)
	list_filter = ('carros', 'fabricante')
	ordering = ('fabricante',)

class AdminCarroUsuario(admin.ModelAdmin):
	list_display = ('usuario','carro')
	search_field = ('usuario',)
	list_filter = ('usuario','carro')
	ordering = ('usuario',)

admin.site.register(Marca,AdminMarca)
admin.site.register(Carro,AdminCarro)
admin.site.register(Fabricante,AdminFabricante)
admin.site.register(Motor,AdminMotor)
admin.site.register(PastilhaFreio,AdminPastilha)
admin.site.register(CarroUsuario,AdminCarroUsuario)
