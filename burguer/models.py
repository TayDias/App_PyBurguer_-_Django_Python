from django.db import models

# A classe Produto é uma herança da classe models.Model
class Produto(models.Model):
    descricao = models.TextField(null=False, blank=False)  # Atributo descricao do tipo models.TextField (tipo texto)
    preco = models.FloatField(null=False, blank=False)   # Atributo preco do tipo models.FloatField (tipo float)
    imagem = models.ImageField(upload_to='burguer/img', default='', null=False, blank=False)

    # Método de aoresentação do conteúdo no Django Admin
    def __str__(self):
        return self.descricao