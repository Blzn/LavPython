from django.contrib.auth.forms import User
from django import forms
from forms import *
from models import *

class FormTrocaPeca(forms.ModelForm):
	class Meta:
		model = CarroUsuario
		exclude = ('usuario',
			   'ultimoUpdate',
			   'quilometragem',
			   'kmMotor',
			   'kmPastilha',
			   'carro')

		def save(self,commit=True):
			carroUsuario = super(FormTrocaPeca,self).save(commit=False)
			carroUsuario.save()
		


class FormCarroUsuario(forms.ModelForm):
	class Meta:
		model = CarroUsuario
		exclude = ('usuario','ultimoUpdate')
	
	marca = forms.ModelChoiceField(Marca.objects.all(), widget=forms.Select(), required=True)
	
	def __init__(self, *args, **kwargs):
		self.base_fields['carro'].choices = ""
		self.base_fields['motor'].choices = ""
		self.base_fields['pastilhaFreio'].choices = ""
		super(FormCarroUsuario, self).__init__(*args,**kwargs)
	
	"""Passando-se o ultimoUpdate através da view. Com isso, fica mais fácil fazer demonstrações, embora o default seja passar como argumento na view date.today()""" 
	def save(self, usuario,ultimoUpdate,commit=True):
		carroUsuario = super(FormCarroUsuario, self).save(commit=False)
		
		carroUsuario.usuario = usuario
		carroUsuario.ultimoUpdate = ultimoUpdate
		
		if commit:
			carroUsuario.save()
        
		return carroUsuario
