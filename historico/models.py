from django.db import models

# Create your models here.
class HistoricoTroca(models.Model):
    carro = models.ForeignKey(CarroUsuario)
    pecaDe = models.ForeignKey(Peca)
    saudePeca = models.IntegerField()
    pecaPara = models.ForeignKey(Peca)
    

