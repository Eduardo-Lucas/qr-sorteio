import uuid

from django.db import models
from django.urls import reverse


class Cadastro(models.Model):
    nome_completo = models.CharField(max_length=50, unique=True,
                                     help_text='Informe seu nome completo')
    email = models.EmailField(max_length=50, unique=True,
                              help_text='Informe seu endereço de E-mail')
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    codigo = models.UUIDField(primary_key=False
                              , default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.nome_completo
    
    def get_absolute_url(self):
        return reverse('cadastro_detail', args={self.id})
        
    class Meta:
        ordering = ['nome_completo']
