from django.db import models
from carro.models import CarroUsuario
from trajeto.models import Trajeto

# Create your models here.
TIPO_DIA = (
    ('T','Todos'),
    ('SU','Semana util'),
    ('DS','Data Selecionada'),
    ('FS','Fins de semana'),
    ('DE','Dias Especificos'),
    )

class Dia(models.Model):
    trajeto = models.ForeignKey(Trajeto)
    carro = models.ForeignKey(CarroUsuario)
    data = models.DateField(blank=True,null=True)
    dias = models.CommaSeparatedIntegerField(max_length = 14, null=True, blank=True)
    tipo = models.CharField(choices = TIP O_DIA,max_length = 30)
    consumo = models.DecimalField(max_digits = 10,decimal_places=2)
    idaEVolta = models.BooleanField()

    class Meta:
        ordering = ['-data']
    
