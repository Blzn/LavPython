from django.contrib.auth.forms import User
from django import forms
from forms import *
from models import *

class FormCarroUsuario(forms.ModelForm):
	class Meta:
		model = CarroUsuario
		exclude = ('usuario')
	
	marca = forms.ModelChoiceField(Marca.objects.all(), widget=forms.Select(), required=True)
	
	def __init__(self, *args, **kwargs):
		self.base_fields['carro'].choices = ""
		self.base_fields['motor'].choices = ""
		self.base_fields['pastilhaFreio'].choices = ""
		super(FormCarroUsuario, self).__init__(*args,**kwargs)
	
	def save(self, usuario, commit=True):
		carroUsuario = super(FormCarroUsuario, self).save(commit=False)
		
		carroUsuario.usuario = usuario
		
		if commit:
			carroUsuario.save()
        
		return carroUsuario