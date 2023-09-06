from django.db import models

# Create your models here.
class Carro(models.Model):
    tipo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    marca  =models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    preco = models.FloatField()
    ano = models.DateField()
    km = models.FloatField()
    pagamento = models.CharField(max_length=100)
    leilao = models.BooleanField()
    

def retornar_todos_os_dados():
    carros = Carro.objects.all()
    return carros
    