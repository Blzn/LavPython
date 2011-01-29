from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import FormDia
from django.http import HttpResponseRedirect
from carro.models import CarroUsuario

def associar(request):
    carro = CarroUsuario.objects.get(id=1)
    if request.method == 'POST':
        form = FormDia(request.POST)
        if form.is_valid():
            novo_dia = form.save(carro)
            print novo_dia.dias
            return HttpResponseRedirect('/')
    else:
        form = FormDia()
    

    return render_to_response(
        'associar.html',
        locals(),
        context_instance=RequestContext(request))
