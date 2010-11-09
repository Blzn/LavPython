from django.db import models
from django.contrib.admin.models import User
from django.contrib.localflavor.br.br_states import STATE_CHOICES

SEXO_C = (('F','Feminino'),('M','Masculino'),)


class Cadastro(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, editable = False)
    
    nome = models.CharField(max_length = 255)
    sobrenome = models.CharField(max_length = 255)
    sexo = models.CharField(max_length = 1, choices = SEXO_C)
    dataNascimento = models.DateField(verbose_name = 'Data de Nascimento', 
                                      blank = True, null = True)
    email = models.EmailField(max_length = 255)
    senha  = models.CharField(max_length = 30)
    endereco = models.CharField(max_length = 255, verbose_name = u'Endereço',
                                blank = True, null = True)
    num = models.CharField(max_length = 10, verbose_name = u'Número', blank = True,
                           null = True)
    complemento = models.CharField(max_length = 255, null = True, blank = True)
    cep = models.CharField(max_length = 9)
    bairro = models.CharField(max_length = 255, blank = True, null = True)
    estado  = models.CharField(choices = STATE_CHOICES, max_length = 2)
    cidade = models.CharField(max_length = 255)
    dataCadastro = models.DateTimeField(auto_now_add = True)
    
    
    class Meta:
        ordering = ['-id']
    
    def save(self):
        if not self.id:
            emailRegistrado = Cadastro.objects.filter(email = self.email).count()
            if emailRegistrado:
                raise EmailExistente
            
            usr = User.objects.filter(username = self.email)
            
            if user:
                u = usr[0]
            else:
                u = User.objects.create_user(self.email, self.email, self.senha)
            
            u.save()
            self.user = u
        else:
            self.user.username = self.email
            self.user.email = self.email
            self.user.set_password(self.senha)
            self.user.save()
        
        
        super(Cadastro, self).save()
        
    def __unicode__(self):
        return self.nome    