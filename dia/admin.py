from django.contrib import admin
from dia.models import Dia

class DiaAdmin(admin.ModelAdmin):
    list_display = ('data','tipo','carro')
    search_fields = ('data',)

admin.site.register(Dia,DiaAdmin)
