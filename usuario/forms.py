# -*- coding: utf-8 -*-
from django.contrib.auth.forms import User
from django import forms
from django.contrib.localflavor.br.br_states import STATE_CHOICES
from forms import *
from models import *



class FormCadastro(forms.ModelForm):
    class Meta:
        model = Usuario
        
    nome = forms.CharField(max_length = 255)
    sobrenome = forms.CharField(max_length = 255)
    sexo = forms.ChoiceField(choices = SEXO_C)
    dataNascimento = forms.DateField(required = False, label = ('Data de Nascimento'))
    email = forms.EmailField(max_length = 255)
    senha  = forms.CharField(max_length = 30, widget = forms.PasswordInput)
    endereco = forms.CharField(max_length = 255,required = False, label = ('Endereço'))
    num = forms.CharField(max_length = 10,required = False, label = ('Número'))
    complemento = forms.CharField(max_length = 255,required = False)
    cep = forms.CharField(max_length = 9)
    bairro = forms.CharField(max_length = 255,required = False)
    estado  = forms.ChoiceField(choices = STATE_CHOICES)
    cidade = forms.CharField(max_length = 255)
    
    def save(self, commit=True):
        usuario = super(FormCadastro, self).save(commit=False)
        
        if commit:
            usuario.save()
        
        return usuario
        
        