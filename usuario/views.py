# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import FormCadastro
from django.http import HttpResponseRedirect, HttpResponse


def registrar(request):
    if request.method == 'POST':
        form = FormCadastro(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            return HttpResponseRedirect('/')
    else:
        form = FormCadastro()
        
    return render_to_response(
                            'cadastro.html',
                            locals(),
                            context_instance=RequestContext(request),
                            )

