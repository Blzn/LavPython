from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import FormDia
from django.http import HttpResponseRedirect
from carro.models import CarroUsuario
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from carro.models import Motor
from models import Dia

@login_required
def associar(request,carro_id,classe):
    carro = CarroUsuario.objects.get(id=carro_id)
    if request.method == 'POST':
        form = FormDia(request.user, request.POST)
        if form.is_valid():
            motor = Motor.objects.get(id=carro.motor_id)
            trajeto = form.cleaned_data['trajeto']
            consumo = motor.kmLitro * trajeto.distancia
            novo_dia = form.save(carro,consumo)
            return HttpResponseRedirect('/')
    else:
        form = FormDia(request.user)

    return render_to_response(
        'associar.html',
        locals(),
        context_instance=RequestContext(request))

@login_required
def editar_dia(request,dia_id,classe):
    dia = Dia.objects.get(id=dia_id)
    carro = CarroUsuario.objects.get(id=dia.carro_id)
    if request.method == 'POST':
        form = FormDia(request.user, request.POST,instance=dia)
        if form.is_valid():
            motor = Motor.objects.get(id=carro.motor_id)
            trajeto = form.cleaned_data['trajeto']
            consumo = motor.kmLitro * trajeto.distancia
            novo_dia = form.save(carro,consumo)
            return HttpResponseRedirect('/')
    else:
        form = FormDia(request.user,instance=dia)

    return render_to_response(
        'associar.html',
        locals(),
        context_instance=RequestContext(request))

		
@login_required
def meus_dias(request, carro_id):
    carro = CarroUsuario.objects.get(id=carro_id)
    dias = carro.dia_set.all()	
    dias_da_semana = ['Seg','Ter','Qua','Qui','Sex','Sab','Dom']

    return render_to_response(
		'meus_dias.html',
		locals(),
		context_instance=RequestContext(request))
