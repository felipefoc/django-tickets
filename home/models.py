from django.db import models
from account.models import Account
from django.conf import settings

# Create your models here.
class TipoTicket(models.Model):
    nome = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome



class SetorTicket(models.Model):
    nome = models.CharField(max_length=30)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

        
class Tickets(models.Model):
    CHOICES = (
        ('Em andamento', 'Em andamento'),
        ('Finalizado', 'Finalizado'),
        ('Pendente', 'Pendente'),
        )

    tipo = models.ForeignKey(TipoTicket, null=True, on_delete=models.CASCADE)
    setor = models.ForeignKey(SetorTicket, null=True, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=CHOICES, null=True)
    descrição = models.TextField(null=True)
    finalizado_em = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='uploads/', null=True)

    
