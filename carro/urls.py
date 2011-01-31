from django.conf.urls.defaults import *

urlpatterns = patterns('carro.views', 
            url(r'addcarro/', 'cad_carro', name = 'cadCarro'),
			url(r'getcarros/', 'get_carros', name = 'getCarros'),
			url(r'getmotores/', 'get_motores', name = 'getMotores'),
			url(r'getpastilhas/', 'get_pastilhas', name = 'getPastilhas'),
            url(r'^meus_carros/$','meus_carros',name='meus_carros'),
            url(r'^troca_pecas/(?P<carro_id>\d+)','troca_pecas', name='troca_pecas'),
            )
