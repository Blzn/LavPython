﻿from django.conf.urls.defaults import *

urlpatterns = patterns('historico.views', 
			url(r'^historico_trocas/', 'exibir_historico_trocas', name='historico_trocas'),
			url(r'^get_trocas/', 'get_trocas',),
            )