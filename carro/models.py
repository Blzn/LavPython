from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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
	kmMax = models.DecimalField(max_digits = 10,decimal_places = 2)

	def __unicode__(self):
		return self.modelo

class Motor(Peca,models.Model):
	cilindros = models.DecimalField(max_digits = 2, decimal_places = 0)
	combustivel = models.CharField(choices = COMBUSTIVEIS, max_length = 30)
	potencia = models.DecimalField(max_digits = 4, decimal_places = 0)
	kmLitro = models.DecimalField(max_digits = 3,decimal_places = 0)
	

class PastilhaFreio(Peca, models.Model):
	cod_fabricante = models.DecimalField(max_digits = 10, decimal_places= 0)

class CarroUsuario(models.Model):
	usuario = models.ForeignKey(User)
	carro = models.ForeignKey(Carro)

	motor = models.ForeignKey(Motor)
	kmMotor = models.DecimalField(max_digits = 10,decimal_places = 2,default=0,verbose_name="Km do motor",help_text="Quilometragem rodada utilizando esse motor")

	pastilhaFreio = models.ForeignKey(PastilhaFreio)
	kmPastilha = models.DecimalField(max_digits = 10,decimal_places=2,default=0,verbose_name="Km da pastilha",help_text="Quilometragem rodada utilizando essa pastilha")

	quilometragem = models.DecimalField(max_digits = 10,decimal_places=2,default=0)
	ultimoUpdate = models.DateField()

	def __unicode__(self):
		return self.carro.modelo
	   
	def get_absolute_url(self):
		return reverse('carrousuario', kwargs={'carro_id': self.id})
