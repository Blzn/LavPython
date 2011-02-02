from django.conf.urls.defaults import *

urlpatterns = patterns('dia.views',
                       url(r'associar/(?P<carro_id>\d+)$','associar',{'classe': 'Dia'},name = 'associar'),
                       url(r'meus_dias/(?P<carro_id>\d+)$','meus_dias',),
                       url(r'editar_dia/(?P<dia_id>\d+)$','editar_dia',{'classe':'Dia'}, name = 'Editar Dia')
					   )
