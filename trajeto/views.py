from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

def trajeto(request):
    parametrobody = u"onload=\"initialize()\""
    return render_to_response(
        'set_trajetos.html',
        locals(),
        context_instance=RequestContext(request),
        )
