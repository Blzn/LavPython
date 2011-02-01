from django.shortcuts import render_to_response
from carro.models import CarroUsuario, Motor,PastilhaFreio
from django.contrib.auth.decorators import login_required
from models import *
from datetime import datetime


def atualiza_historico_troca(form,carro_id):
    carro = CarroUsuario.objects.get(id=carro_id)

    if(form.cleaned_data['trocar_motor']):
        historico = None
        motor_velho = Motor.objects.get(id=carro.motor_id)
        motor_novo = form.cleaned_data['motor']

        historico = HistoricoTroca(carro=carro,dePeca=motor_velho,paraPeca=motor_novo, tipoPeca='MT',desgaste=carro.kmMotor,diaDaTroca=datetime.today().date(),quilometragem=carro.quilometragem)
        historico.save()

    if(form.cleaned_data['trocar_pastilhaFreio']):
        historico = None
        pastilha_velha = PastilhaFreio.objects.get(id=carro.pastilhaFreio_id)
        pastilha_nova = form.cleaned_data['pastilhaFreio']

        historico = HistoricoTroca(carro=carro,dePeca=pastilha_velha,paraPeca=pastilha_nova,tipoPeca='PF',desgaste=carro.kmPastilha,diaDaTroca=datetime.today().date(),quilometragem=carro.quilometragem)
        historico.save()
        
    
