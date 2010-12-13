from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='toFloat')
@stringfilter
def toFloat(valor):
    return valor.replace(',','.')
