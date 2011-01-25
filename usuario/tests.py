from django.test import TestCase

class TesteCadastro(TestCase):
    fixtures = ['test_data.json']

    def test_acesso_cadastro(self):
        response = self.client.get('/usuario/cadastro/')
        self.assertEqual(response.status_code,200)

    def test_post_data(self):
        response = self.client.post('/usuario/cadastro/',{'email': 'teste@teste.com.br', 'senha': '1010','confirme_a_senha': '1010','nome': 'Testante','sexo': 'M','dataNascimento:': '10/10/2010','endereco': 'ali', 'num': 'wut', 'cep': '45400-000','bairro': 'wth','estado': 'BA','cidade':'uaua'})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"cadastro/cadastro.html")

    def test_login(self):
        login = self.client.login(username='artus',password='123456')
        self.assertEqual(login,True)
        
    def test_login_false(self):
        login = self.client.login(username="inexistente",password="naotem")
        self.failIf(login)
    
    
