from django.db import models

class Generos (models.Model):
    genero = models.CharField('Genero', max_length=100)

    def __str__(self) -> str:
        return self.genero

class filmes (models.Model):
    filme = models.CharField('Nome', max_length=100)
    genero = models.ForeignKey('Generos', on_delete=models.PROTECT)
    quantidade = models.IntegerField('Quantidade', default=0)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
