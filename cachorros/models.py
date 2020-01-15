from django.db import models

# Create your models here.

class Cachorro(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    cor_pelo = models.CharField(max_length=255)
    porte = models.CharField(max_length=255)
    dono = models.CharField(max_length=255)