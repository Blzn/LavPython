from django.conf.urls.defaults import *

urlpatterns = patterns('carro.views', 
            url(r'addcarro/', 'cad_carro', ),
            url(r'getcarros/', 'get_carros', ),
            url(r'getmotores/', 'get_motores', ),
            url(r'getpastilhas/', 'get_pastilhas', ),
            url(r'^meus_carros/$','meus_carros',),
            url(r'^troca_pecas/(?P<carro_id>\d+)/$','troca_pecas', ),
			url(r'^carro/(?P<carro_id>\d+)/$','carrousuario', name='carrousuario'),
            )
