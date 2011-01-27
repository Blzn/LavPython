from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline

from models import Marca, Carro, Motor, PastilhaFreio

class AdminMarca(admin.ModelAdmin):
	list_display = ('nome',)

class AdminCarro(admin.ModelAdmin):
	list_display = ('marca', 'modelo')
	search_fields = ('marca',)
	list_filter = ('marca',)

class MotorAdmin(admin.ModelAdmin):
	list_display = ('fabricante','modelo')
	search_fields = ('combustivel','potencia','modelo')
	list_filter = ('modelo',)
	ordering = ('fabricante',)

class PastilhaAdmin(admin.ModelAdmin):
	list_display = ('fabricante','modelo')
	search_fields = ('modelo',)
	ordering = ('fabricante',)

admin.site.register(Marca,AdminMarca)
admin.site.register(Carro,AdminCarro)
admin.site.register(Motor,MotorAdmin)
admin.site.register(PastilhaFreio)
