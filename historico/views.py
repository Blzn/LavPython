# -*- coding: utf-8 -*-
from django.core import serializers
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import HistoricoTroca
from carro.models import CarroUsuario, Peca, Motor, PastilhaFreio, Fabricante
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from functions import *

@login_required
def exibir_historico_trocas(request,carro_id):
    return render_to_response('hist_geral.html',locals(),context_instance = RequestContext(request))

@login_required
def get_trocas(request):
	carro_id = request.GET.get('carro_id','')
	tipo_peca = request.GET.get('tipo_peca','')
	historicos = HistoricoTroca.objects.filter(carro=carro_id,tipoPeca=tipo_peca)
	dados = list()
	for historico in historicos:
		#eu sei que isso eh uma merda...mas foi o preço q pagamos por ter feito Peca abstrato...que odin tenha piedade de nossas almas
		if tipo_peca == 'MT':
			de_peca = Motor.objects.get(id=historico.dePeca_id)
			para_peca = Motor.objects.get(id=historico.paraPeca_id)
		elif tipo_peca == 'PF':
			de_peca = PastilhaFreio.objects.get(id=historico.dePeca_id)
			para_peca = PastilhaFreio.objects.get(id=historico.paraPeca_id)
			
		de_fabricante = Fabricante.objects.get(id=de_peca.fabricante_id)
		para_fabricante = Fabricante.objects.get(id=para_peca.fabricante_id)
		
		troca = Troca()
		troca.dePeca = de_peca.modelo,
		troca.deFabricante = de_fabricante.nome,
		troca.paraPeca = para_peca.modelo,
		troca.paraFabricante = para_fabricante.nome,
		troca.desgaste = historico.desgaste,
		troca.diaDaTroca = historico.diaDaTroca.strftime("%Y %b %d"),
		troca.quilometragem = historico.quilometragem
		dados.append(troca)
	retorno = json_repr(dados)

	return HttpResponse(retorno, mimetype="text/javascript")
