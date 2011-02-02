# -*- coding: utf-8 -*-
from django.contrib.auth.forms import User
from django import forms
from django.contrib.localflavor.br.br_states import STATE_CHOICES
from forms import *
from models import *

class FormLogin(forms.Form):
    email = forms.EmailField(max_length=255)
    senha = forms.CharField(max_length = 30, widget = forms.PasswordInput)

class FormEdit(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ('user','email','senha',)

    def save(self, commit=True):
         usuario = super(FormEdit, self).save(commit=False)
        
         if commit:
             usuario.save()
             
         return usuario
    


class FormCadastro(forms.ModelForm):
    class Meta:
        model = Usuario
		#fields = ('nome','sobrenome','sexo','dataNascimento','email','senha','endereco','num','complemento','cep','bairro','estado','cidade','dataCadastro')
		
    confirme_a_senha = forms.CharField(max_length=30, widget=forms.PasswordInput, label='confirma senha')
	
    def clean_email(self):
		if User.objects.filter(username = self.cleaned_data['email'],).count():
			raise forms.ValidationError('Ja existe um usuario com este email')
	
		return self.cleaned_data['email']
		
    def clean_confirme_a_senha(self):
		if self.cleaned_data['confirme_a_senha'] != self.data['senha']:
			raise forms.ValidationError('Confirmacao da senha nao confere!')
		
		return self.cleaned_data['confirme_a_senha']

    def __init__(self,*args,**kwargs):
        self.base_fields['senha'].help_text = 'Informe uma senha segura'
        self.base_fields['senha'].widget = forms.PasswordInput()
        super(FormCadastro, self).__init__(*args,**kwargs)

    def save(self, commit=True):
        usuario = super(FormCadastro, self).save(commit=False)
        
        if commit:
            usuario.save()
        
        return usuario
    

            
    
