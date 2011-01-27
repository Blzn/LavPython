from django.db import models
from django.contrib.auth.models import User

COMBUSTIVEIS = (
	('A','Alcool'),
	('G','Gasolina'),
	('D','Diesel'),
	('N','Gas Natural'),
	)


class Marca(models.Model):
	nome = models.CharField(max_length = 255)
	
	def __unicode__(self):
		return self.nome

class Carro(models.Model):
	marca = models.ForeignKey('Marca',)
	modelo = models.CharField(max_length = 255)
#	motor = models.ForeignKey('Motor')
#	partilhaFreio = models.ForeignKey('PastilhaFreio')

	def __unicode__(self):
		return self.modelo

class Fabricante(models.Model):
	nome = models.CharField(max_length = 255)
	
	def __unicode__(self):
		return self.nome
		
class Peca(models.Model):
	class Meta:
		abstract = True

	modelo = models.CharField(max_length = 255)
	fabricante = models.ForeignKey('Fabricante')
	carros = models.ManyToManyField(Carro,blank=True,null=True)

	def __unicode__(self):
		return self.modelo

class Motor(Peca,models.Model):
	cilindros = models.DecimalField(max_digits = 2, decimal_places = 0)
	combustivel = models.CharField(choices = COMBUSTIVEIS, max_length = 30)
	potencia = models.DecimalField(max_digits = 4, decimal_places = 0)
	

class PastilhaFreio(Peca, models.Model):
	cod_fabricante = models.DecimalField(max_digits = 10, decimal_places= 0)

class CarroUsuario(models.Model):
	usuario = models.ForeignKey(User)
	carro = models.ForeignKey(Carro)
	motor = models.ForeignKey(Motor)
	pastilhaFreio = models.ForeignKey(PastilhaFreio)

