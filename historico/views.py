from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *
from carro.models import CarroUsuario,Pastilha,Motor
from django.contrib.auth.decorators import login_required



