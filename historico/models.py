from django.db import models

# Create your models here.
class HistoricoCarro(models.Model):
    kmCarro = models.DecimalField(max_digits = 10, decimal_places = 2)
    trocasMotor = models.IntegerField()
    trocasPastilha = models.IntegerField()
    consumoSemanal = models.DecimalField(max_digits = 5, decimal_places = 2)
    

class HistoricoGeral(models.Model):
    kmTotal = models.DecimalField(max_digits = 10, decimal_places = 2)
    trocas = models.IntegerField()
    mediaTrajetos = models.IntegerField()
    
