from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import FormDia

def associar(request):
    form = FormDia()

    return render_to_response(
        'associar.html',
        locals(),
        context_instance=RequestContext(request))
