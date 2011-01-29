from django import forms
from models import *


DIAS_SEMANA = (
    (1,'Domingo'),
    (2,'Segunda'),
    (3,'Terca'),
    (4,'Quarta'),
    (5,'Quinta'),
    (6,'Sexta'),
    (7,'Sabado'),
    )


class TextCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, **kwargs):
        if isinstance(value, basestring):
            value = value.split(",")
        return super(TextCheckboxSelectMultiple, self).render(name, value, **kwargs)

class TextMultiField(forms.MultipleChoiceField):
    widget = TextCheckboxSelectMultiple
    def clean(self, value):
        val = super(TextMultiField, self).clean(value)
        return ",".join(val)


class FormDia(forms.ModelForm):
    class Meta:
        model = Dia
        exclude = ('carro','dias',)

    dias = TextMultiField(choices=DIAS_SEMANA,)

    

    def save(self,carro,commit=True):
        dia = super(FormDia,self).save(commit=False)

        dia.carro = carro
        
        if commit:
            dia.save()

        return dia
  
