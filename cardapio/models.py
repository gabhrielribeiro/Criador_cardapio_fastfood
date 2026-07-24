from django.db import models
from django.contrib.auth.models import User




class Cardapio(models.Model):
    dono = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cardapios",
        null=True,
        blank=True,
    )
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    banner = models.ImageField(upload_to='banner/', null=True, blank=True)
    lanchonete = models.CharField(max_length=50)
    endereco = models.TextField()
    disponivel = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.lanchonete
    


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    cardapio = models.ForeignKey(
        Cardapio,
        on_delete=models.CASCADE,
        related_name="categorias", 
    )

    def __str__(self):
        return self.nome


class Produto(models.Model):
    capa = models.ImageField(upload_to="foto_produto/")
    titulo = models.CharField(max_length=50)
    desc = models.CharField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="produto", blank=True, null=True
    )
    cardapio = models.ForeignKey(
        Cardapio, on_delete=models.CASCADE, related_name="produtos", blank=True, null=True
    )

    def __str__(self):
        return self.titulo
