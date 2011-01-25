from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from models import *

@login_required
def meus_trajetos(request):
	trajetos = Trajeto.objects.filter(usuario=request.user)
	return render_to_response('meus_trajetos.html', locals(), context_instance = RequestContext(request),)


@login_required
def editar_trajeto(request):
    trajeto_teste = Trajeto.objects.get(id=6)
    nome = trajeto_teste.nome
    distancia = trajeto_teste.distancia
    cord_teste = trajeto_teste.coordenadas_set.all()

    return render_to_response(
        'edit_trajeto.html',
        locals(),
        context_instance=RequestContext(request))


@login_required
def trajeto(request):
    if request.method == 'POST':
        nome_trajeto = request.POST.get('nome')
        '''Lembrar de depois tratar o erro para distancia 0
        Fazer funcao parser dps :B'''
        distancia_total = request.POST.get('distancia')
        distancia_total = distancia_total[:-2].replace(',','.')
        coordenadas_todas = request.POST.getlist('waypoints')
	
        
        novo_trajeto = Trajeto(nome=nome_trajeto, distancia=distancia_total,usuario= request.user)
        novo_trajeto.save()

        for coordenada in coordenadas_todas:
            tupla_coordenada = coordenada[1:-1].split(',')
            temp_latitude = tupla_coordenada[0]
            temp_longitude = tupla_coordenada[1]
            nova_coordenada = Coordenadas(latitude=temp_latitude, longitude= temp_longitude, trajeto=novo_trajeto)
            nova_coordenada.save()

        

    return render_to_response(
        'set_trajetos.html',
        locals(),
        context_instance=RequestContext(request),
        )
