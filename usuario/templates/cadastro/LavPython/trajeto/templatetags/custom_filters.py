from django import template

register = template.Library()

@register.filter(name='toFloat')
def toFloat(valor):
    return valor.replace(',','.')
