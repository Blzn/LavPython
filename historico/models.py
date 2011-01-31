from django.db import models

# Create your models here.
class HistoricoTroca(models.Model):
    carro = models.ForeignKey(CarroUsuario)
    dePeca = models.ForeignKey(Peca)
    paraPeca = models.ForeignKey(Peca)
    saudePeca = models.FloatField()
    diaDaTroca = models.DateTimeField()
    quilometragem = models.FloatField()
