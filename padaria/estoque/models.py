from django.db import models

# Create your models here.class Padarias(models.Model):
class Produtos(models.Model):
    produto = models.CharField('Produto', max_length=100)
    quantidade = models.DecimalField('Quantidade', max_digits=12, decimal_places=2)
    preco = models.DecimalField('Preço', max_digits=12, decimal_places=2)
