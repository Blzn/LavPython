from django.db import models
from django.contrib.auth.models import User

class Dia(models.Model):
    data = models.DateField(blank=True,null=True)

    class Meta:
        ordering = ['-data']

class Coordenadas(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()

	class Meta:
		ordering = ['id']		
		

class Trajeto(models.Model):
    nome = models.CharField(max_length = 120)
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User)
    coordenadas = models.ForeignKey(Coordenadas)
	
    class Meta:
        ordering = ['nome']
