from django.conf.urls.defaults import *

urlpatterns = patterns('trajeto.views', 
			url(r'^cadtrajeto/$', 'trajeto', name='cadastrar_trajeto'),
			url(r'^editrajeto/(?P<trajeto_id>\d+)$','editar_trajeto',{'classe': 'Trajeto'}, name='editar_trajeto'),
            url(r'^meus_trajetos/$','meus_trajetos',name='meus_trajetos'),

            )
