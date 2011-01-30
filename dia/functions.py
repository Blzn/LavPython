from datetime import datetime, timedelta
from carro.models import CarroUsuario
from trajeto.models import Trajeto
from models import Dia

dias_uteis = [0, 1, 2, 3, 4]
fim_de_semana = [5,6]

def atualiza_carros(usuario, data = datetime.today().date()):
	carros = CarroUsuario.objects.filter(usuario=usuario)
	for carro in carros:
		carroDiaTrajetos = Dia.objects.filter(carro=carro)
		for dia in daterange(carro.ultimoUpdate,data):
			for carroDiaTrajeto in carroDiaTrajetos: 
				if verifica_dia_trajeto(carroDiaTrajeto,dia):
					trajeto = Trajeto.objects.get(id=carroDiaTrajeto.trajeto_id)
					if carroDiaTrajeto.idaEVolta:
						distancia = trajeto.distancia * 2
					else:
						distancia = trajeto.distancia
					carro.quilometragem += distancia
					carro.kmMotor += distancia
					carro.kmPastilha += distancia				
		carro.ultimoUpdate = data
		carro.save()

def verifica_dia_trajeto(carroDiaTrajeto,dia):
	if carroDiaTrajeto.tipo == 'T' :
		return True
	if carroDiaTrajeto.tipo == 'SU' and dia.weekday() in dias_uteis:
		return True
	if carroDiaTrajeto.tipo == 'FS' and dia.weekday() in fim_de_semana:
		return True
	if carroDiaTrajeto.tipo == 'DS' and carroDiaTrajeto.data == dia:
		return True
	if carroDiaTrajeto.tipo == 'DE' and str(dia.weekday()) in carroDiaTrajeto.dias.split(','):
		return True
	return False
	


	
def daterange(start_date, end_date):
	"""http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
		VALEU, MANOLOS!"""
	for n in range((end_date - start_date).days):
		yield start_date + timedelta(n)
