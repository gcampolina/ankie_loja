from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome

class CarrinhoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    tamanho = models.CharField(max_length=10)


    def subtotal(self):
        return self.quantidade * self.produto.preco

class CustomUser(AbstractUser):
    celular = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username