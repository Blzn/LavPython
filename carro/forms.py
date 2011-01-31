from django.contrib.auth.forms import User
from django import forms
from forms import *
from models import *
from datetime import date

class FormTrocaPeca(forms.ModelForm):
	class Meta:
		model = CarroUsuario
		exclude = ('usuario',
			   'ultimoUpdate',
			   'carro',
			   'quilometragem',
			   'kmMotor',
			   'kmPastilha'
			   )
		
	trocar_motor = forms.BooleanField(required=False,initial=False,)
	trocar_pastilhaFreio = forms.BooleanField(required=False,initial=False,)
		
	def save(self,commit=True):
		carroUsuario = super(FormTrocaPeca,self).save(commit=False)
		if self.cleaned_data['trocar_motor']:
			carroUsuario.kmMotor = 0
		if self.cleaned_data['trocar_pastilhaFreio']: 
			carroUsuario.kmPastilha = 0
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
	def save(self, usuario,ultimoUpdate=date.today(),commit=True):
		carroUsuario = super(FormCarroUsuario, self).save(commit=False)
		
		carroUsuario.usuario = usuario
		carroUsuario.ultimoUpdate = ultimoUpdate
		
		if commit:
			carroUsuario.save()
        
		return carroUsuario
