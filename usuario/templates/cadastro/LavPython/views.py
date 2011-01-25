from django.shortcuts import render_to_response
from django.template import RequestContext
from usuario.forms import FormLogin
from django.contrib import auth
from django.http import HttpResponseRedirect



def home(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        senha = request.POST.get('senha','')
        user = auth.authenticate(username=email,password=senha)
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")

    else:
        formLog = FormLogin()
    return render_to_response("home.html",locals(),context_instance=RequestContext(request))
