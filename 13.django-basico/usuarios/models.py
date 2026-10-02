from django.db import models

class Clientes(models.Model):
    queixa_choices = (
        ('D', 'Depressão'),
        ('A', 'Ansiedade')
    )

    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    queixa = models.CharField(max_length=1, choices=queixa_choices)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    foto = models.ImageField(upload_to='media/foto_cliente', null=True, blank=True)


    def __str__(self):
        return self.nome