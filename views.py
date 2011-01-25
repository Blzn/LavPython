from django.shortcuts import render_to_response
from django.template import RequestContext
from usuario.forms import FormLogin
from django.contrib import auth
from django.http import HttpResponseRedirect


def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
		
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')
		
def logout(request):
	logout(request)
	return HttpResponseRedirect('/')
		
def home(request):

    return render_to_response("home.html",locals(),context_instance=RequestContext(request))
