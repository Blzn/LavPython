from django.conf.urls.defaults import *

urlpatterns = patterns('dia.views',
                       url(r'associar/','associar',name = 'associar'),
                       )
