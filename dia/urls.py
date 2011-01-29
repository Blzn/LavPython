from django.conf.urls.defaults import *

urlpatterns = patterns('dia.views',
                       url(r'associar/(?P<carro_id>\d+)$','associar',{'classe': 'Dia'},name = 'associar'),
                       )
