from django.shortcuts import render_to_response
from models import *

@login_required
def cad_carro(request):
    if request.method == 'POST':
        
