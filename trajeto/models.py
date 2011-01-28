from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Trajeto(models.Model):
    nome = models.CharField(max_length = 120)
    distancia = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User)
	
    def get_absolute_url(self):
		return reverse('editar_trajeto', kwargs={'trajeto_id': self.id})

    def __unicode__(self):
        return self.nome
	
    class Meta:
        ordering = ['nome']
		
class Coordenadas(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()
	trajeto = models.ForeignKey(Trajeto)

	class Meta:
		ordering = ['id']		
		
