from django import forms
from models import *
from trajeto.models import Trajeto


DIAS_SEMANA = (
    (0,'Segunda'),
    (1,'Terca'),
    (2,'Quarta'),
    (3,'Quinta'),
    (4,'Sexta'),
    (5,'Sabado'),
    (6,'Domingo'),
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
        exclude = ('carro','dias','consumo',)
    
    dias_ = TextMultiField(choices=DIAS_SEMANA,)

    def __init__(self, usuario_id, *args, **kwargs):
        self.base_fields['trajeto'].choices = Trajeto.objects.filter(usuario = usuario_id).values_list('pk','nome')
        super(FormDia, self).__init__(*args, **kwargs)


    def save(self,carro,consumo,commit=True):
        dia = super(FormDia,self).save(commit=False)
        dia.dias = self.cleaned_data['dias_']
        dia.carro = carro
        dia.consumo = consumo
        
        if commit:
            dia.save()

        return dia
