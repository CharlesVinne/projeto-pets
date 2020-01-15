from django.db import models
from dono.models import Dono
# Create your models here.

class Cachorro(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    cor_pelo = (
        ('PRETO', 'Preto'),
        ('BRANCO', 'Branco'),
        ('LARANJA', 'Laranja'),
        ('CINZA', 'Cinza'),
        ('TRICOLOR', 'Tricolor'),
        ('BEGE', 'Bege'),
    )
    cor = models.CharField(choices=cor_pelo, max_length=100)
    dono = models.ManyToManyField(Dono)
    portes = (
        ('PEQUENO', 'Pequeno'),
        ('MEDIO', 'Medio'),
        ('GRANDE', 'Grande'),

    )
    porte = models.CharField(choices=portes,max_length=100 )