from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from django.http import HttpResponseRedirect

def trajeto(request):
    if request.method == 'POST':
        testepunk = request.POST.get('dados',False)

    return render_to_response(
        'set_trajetos.html',
        locals(),
        context_instance=RequestContext(request),
        )
