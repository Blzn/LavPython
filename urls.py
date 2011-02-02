from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^LavPython/', include('LavPython.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$','views.home',),
    (r'^contato/$','contato.views.contato'),
    (r'^usuario/', include('usuario.urls')),
	(r'^trajeto/', include('trajeto.urls')),
	(r'^carro/', include('carro.urls')),
    (r'^entrar/$','views.login', ),
    (r'^sair/$',logout,{'template_name': 'sair.html'}, 'sair'),
    (r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    (r'^dia/',include('dia.urls')),
	(r'^historico/',include('historico.urls')),
)
