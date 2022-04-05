from django.db import models

class Pessoas(models.Model):
    nome = models.CharField('Nome', max_length=200)
    telefone = models.CharField('Telefone', max_length=11)
    idade = models.IntegerField('Idade', null=True, blank=True) #o blank que ele aceita um valor branco 

    def __str__(self):
        return self.nome
    class Meta:
        
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome']
 
# Create your models here.
