from django.shortcuts import render_to_response
from carro.models import CarroUsuario, Motor,PastilhaFreio
from django.contrib.auth.decorators import login_required
from models import *
from datetime import *
import json


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
        
class Troca():
    dePeca = None
    paraPeca = None
    tipoPeca = None
    desgaste = None
    diaDaTroca = None
    quilometragem = None


def json_repr(obj):
  """Represent instance of a class as JSON.
  Arguments:
  obj -- any object
  Return:
  String that reprent JSON-encoded object.
  """
  def serialize(obj):
    """Recursively walk object's hierarchy."""

    
    if isinstance(obj, (bool, int, long, float, basestring)):
        return obj
    elif isinstance(obj, dict):
        obj = obj.copy()
        for key in obj:
            obj[key] = serialize(obj[key])
        return obj
    elif isinstance(obj, list):
        return [serialize(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(serialize([item for item in obj]))
    elif hasattr(obj, '__dict__'):
        return serialize(obj.__dict__)
    else:
      return repr(obj) # Don't know how to handle, convert to string
  return json.dumps(serialize(obj))
