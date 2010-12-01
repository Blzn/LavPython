from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import FormContato

def contato(request):
    if request.method == 'POST':
        form = FormContato(request.POST)

        if form.is_valid():
            form.enviar()
            mostrar = 'Seu contato foi enviado e vai ser lido em breve por um de nossos administradores'
    else:
        form = FormContato()

    return render_to_response(
        'contato.html',
        locals(),
        context_instance=RequestContext(request),
        )
