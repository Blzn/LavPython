"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class TesteContato(TestCase):


    def test_envio_contato(self):
        from django.core import mail
        
        mail.send_mail(
            subject = "titulo teste",
            message = "qualquer coisa",
            from_email = "lavoura.car@gmail.com",
            recipient_list=["lavoura.car@gmail.com"],
            fail_silently=False
            )

        self.assertEquals(len(mail.outbox),1)
        self.assertEquals(mail.outbox[0].subject,'titulo teste')

    def test_acesso_contato(self):
        from django.test.client import Client

        client = Client()
        response = client.get('/contato/')
        self.assertEqual(response.status_code,200)

    def test_envio_form(self):
        from django.test.client import Client
        from contato.views import contato
        
        c = Client()
        c.post('/contato/',{'nome': 'mococa','email':'teste@teste.com','mensagem':'lolq'})
        
        from django.core import mail

        self.assertEqual(len(mail.outbox),1)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

