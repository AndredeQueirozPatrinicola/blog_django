from email.mime import image
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Categorias(models.Model):
    titulo_categoria = models.CharField(max_length=20, verbose_name="titulo da categoria")
    descricao_categoria = models.CharField(max_length=100, verbose_name="descrição da categoria")
    imagem_categoria = models.ImageField()




class Posts(models.Model):
    titulo_post = models.CharField(max_length=20, verbose_name="titulo do post")
    sub_titulo = models.CharField(max_length=100, verbose_name="subtitulo do post")
    post = models.CharField(max_length=1000, verbose_name="post")
    imagem_post = models.ImageField()
    categoria = models.ForeignKey(on_delete=CASCADE)