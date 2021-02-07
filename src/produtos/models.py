from django.db import models

# Create your models here.
class Produto(models.Model):
    descricao = models.CharField(max_length=255, null=True)
    categoria = models.CharField(max_length=255, null=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()
