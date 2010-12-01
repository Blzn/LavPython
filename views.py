from django.shortcuts import render_to_response
from django.template import RequestContext
from usuario.forms import FormLogin

def home(request):
    form = FormLogin()
    return render_to_response("home.html",locals(),context_instance=RequestContext(request))
