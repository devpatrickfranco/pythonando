from django.db import models
from django.utils.safestring import mark_safe


class Sintomas(models.Model):
    nome = models.CharField(max_length=255)

    possivel_causa = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nome


class Clientes(models.Model):
    queixa_choices = (
        ('D', 'Depressão'),
        ('A', 'Ansiedade'),
    )

    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    queixa = models.CharField(max_length=1,choices=queixa_choices)
    data_criacao = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='foto_cliente', null=True, blank=True)
    sintomas = models.ManyToManyField(Sintomas, through='ClienteSintoma')

    def __str__(self):
        return self.nome

    @mark_safe
    def get_foto(self):
        if not self.foto:
            return ''
        return f"<img width='30px' src='{self.foto.url}'>"

class ClienteSintoma(models.Model):
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    sintoma = models.ForeignKey(Sintomas,on_delete=models.CASCADE)
    inicio = models.DateField()

    def __str__(self):
        return f'{self.cliente} - {self.sintoma} ...'

