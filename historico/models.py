from django.db import models
from carro.models import CarroUsuario,Peca
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

TIPO_PECA = (
    ('MT','Motor'),
    ('PF','Pastilha de Freio'),
    )

# Create your models here.
class HistoricoTroca(models.Model):
    carro = models.ForeignKey(CarroUsuario)

    content_type = models.ForeignKey(ContentType)
    dePeca_id = models.PositiveIntegerField()
    dePeca = generic.GenericForeignKey('content_type','dePeca_id')

    paraPeca_id = models.PositiveIntegerField()
    paraPeca = generic.GenericForeignKey('content_type','paraPeca_id')

    tipoPeca = models.CharField(choices = TIPO_PECA, max_length = 5)
    desgaste = models.FloatField()
    diaDaTroca = models.DateTimeField()
    quilometragem = models.FloatField()
