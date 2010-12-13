from django.db import models

class Dia(models.Model):
    data = models.DateField(blank=True,null=True)

    class Meta:
        ordering = ['-data']

class Trajeto(models.Model):
    nome = models.CharField(max_length = 120)
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ['nome']

class Coordenadas(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    trajeto = models.ForeignKey(Trajeto)
    
    class Meta:
        ordering = ['id']
