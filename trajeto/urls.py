from django.conf.urls.defaults import *

urlpatterns = patterns('trajeto.views', 
			url(r'^cadtrajeto/$', 'trajeto', name='Cadastrar Trajeto'),
			url(r'^editrajeto/$','editar_trajeto', name='Editar Trajeto'),
                        url(r'^meus_trajetos/$','meus_trajetos',name='Meus Trajetos'),

            )
