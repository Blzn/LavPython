from django import forms
from models import *

DIAS_SEMANA = (
    ('1,','Domingo'),
    ('2,','Segunda'),
    ('3,','Terca'),
    ('4,','Quarta'),
    ('5,','Quinta'),
    ('6,','Sexta'),
    ('7,','Sabado'),
    )

class FormDia(forms.ModelForm):
    class Meta:
        model = Dia
        exclude = ('carro','dias',)

    dias = forms.MultipleChoiceField(choices= DIAS_SEMANA,widget=forms.CheckboxSelectMultiple())

    

    def save(self,carro,commit=True):
        dia = super(FormDia,self).save(commit=False)

        dia.carro = carro
        

        if commit:
            print dia.dias
            dia.save()

        return dia
    
