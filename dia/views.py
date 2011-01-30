from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import FormDia
from django.http import HttpResponseRedirect
from carro.models import CarroUsuario
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def associar(request,carro_id,classe):
    carro = CarroUsuario.objects.get(id=carro_id)
    if request.method == 'POST':
        form = FormDia(request.POST)
        if form.is_valid():
            #motor = Motor.objects.get(id=carro.motor_id)
            consumo = 3
            novo_dia = form.save(carro,int(consumo))
            print novo_dia.dias
            return HttpResponseRedirect('/')
    else:
        form = FormDia(request.user)
    

    return render_to_response(
        'associar.html',
        locals(),
        context_instance=RequestContext(request))
