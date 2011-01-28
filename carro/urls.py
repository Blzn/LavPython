from django.conf.urls.defaults import *

urlpatterns = patterns('carro.views', 
            url(r'addcarro/', 'cad_carro', name = 'cadCarro'),
			url(r'getcarros/', 'get_carros', name = 'getCarros'),
			url(r'getmotores/', 'get_motores', name = 'getMotores'),
			url(r'getpastilhas/', 'get_pastilhas', name = 'getPastilhas'),
            )