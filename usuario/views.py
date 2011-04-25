# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from forms import FormCadastro, FormEdit
from usuario.models import Usuario
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.utils import ConnectionHandler, ConnectionRouter, load_backend, DEFAULT_DB_ALIAS, DatabaseError, IntegrityError

#@transaction.commit_on_success
#def registrar(request):
#    if request.method == 'POST':
#        form = FormCadastro(request.POST)
#        if form.is_valid():
#            novo_usuario = form.save()
#            return HttpResponseRedirect('/')
#    else:
#        form = FormCadastro()
#        
#    return render_to_response(
#                            'cadastro/cadastro.html',
#                            locals(),
#                            context_instance=RequestContext(request),
#                            )



@transaction.commit_manually
def registrar(request):
    if request.method == 'POST':
        form = FormCadastro(request.POST)
        try:
            if form.is_valid():
                novo_usuario = form.save(commit=True)
                novo_usuario.save()
        except IntegrityError:
            transaction.rollback()
        else:
            transaction.commit()
            return HttpResponseRedirect('/')
    else:
        form = FormCadastro()
       
    return render_to_response(
                            'cadastro/cadastro.html',
                            locals(),
                            context_instance=RequestContext(request),
                            )

@transaction.commit_on_success
def edituser(request):
    if request.method == 'POST':
        usuario = Usuario.objects.get(user=request.user)
        form = FormEdit(request.POST,instance=usuario)
        if form.is_valid():
            usuario_edit = form.save(commit=False)
            usuario_edit.user = request.user
            usuario_edit.save()
            return HttpResponseRedirect('/')
    else:
        usuario = Usuario.objects.get(user=request.user)
        form = FormEdit(instance=usuario)
        
        #form = FormCadastro(instance=request.user)
    return render_to_response('editar/editar.html',
                            locals(),
                            context_instance=RequestContext(request),)
	
