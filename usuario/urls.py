from django.conf.urls.defaults import *

urlpatterns = patterns('usuario.views', 
            url(r'cadastro/', 'registrar', name = 'usuario'),
            url(r'update/', 'edituser', name = 'edituser'),
            )