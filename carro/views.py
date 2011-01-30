from django.core import serializers
from django.shortcuts import render_to_response
from models import *
from django.contrib.auth.decorators import login_required
from forms import *
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404, HttpResponse
from datetime import date

@login_required
def minhas_pecas(request,carro_id,classe):
	carro = CarroUsuario.objects.get(id=carro_id)
	motor = Motor.objects.get(id=carro.motor_id)
	pastilha = PastilhaFreio(id=carro.pastilhaFreio_id)
	



@login_required
def meus_carros(request):
	carros = CarroUsuario.objects.filter(usuario=request.user)
	return render_to_response('meus_carros.html',locals(),context_instance = RequestContext(request))


@login_required
def cad_carro(request):

	if request.method == 'POST':
		form = FormCarroUsuario(request.POST)
		if form.is_valid():
			"Pode ser passado qualquer data. Essa é default"
			novo_carro = form.save(request.user,date.today())
			return HttpResponseRedirect('/')
	else:
		form = FormCarroUsuario()
        
	return render_to_response(
                            'addcarro.html',
                            locals(),
                            context_instance=RequestContext(request),
                            )

@login_required
def get_carros(request):

	id_marca = request.GET.get('id_marca', '')
	carros = Carro.objects.filter(marca = int(id_marca))
	retorno = serializers.serialize("json",  carros)
	return HttpResponse(retorno, mimetype="text/javascript")
	
@login_required
def get_motores(request):
	id_carro = request.GET.get('id_carro', '')
	motores = Carro.objects.get(id = int(id_carro)).motor_set.all()
	retorno = serializers.serialize("json", motores)
	return HttpResponse(retorno, mimetype="text/javascript")
	
@login_required
def get_pastilhas(request):
	id_carro = request.GET.get('id_carro', '')
	carro = Carro.objects.get(id = int(id_carro))
	pastilhas = Carro.objects.get(id = int(id_carro)).pastilhafreio_set.all()
	retorno = serializers.serialize("json", pastilhas)
	return HttpResponse(retorno, mimetype="text/javascript")
