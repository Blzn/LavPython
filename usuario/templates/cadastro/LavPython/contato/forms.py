from django import forms
from django.core.mail import send_mail

class FormContato(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensagem = forms.Field(widget=forms.Textarea)

    def enviar(self):
        titulo = 'Mensagem enviada por form de contato'
        destino = 'lavoura.car@gmail.com'
        texto = """
        Nome: %(nome)s

        E-mail: %(email)s

        Mensagem:
        %(mensagem)s
        """ % self.cleaned_data

        send_mail(
            subject = titulo,
            message = texto,
            from_email = destino,
            recipient_list=[destino],
            )
