from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categorias(models.Model):
    titulo_categoria = models.CharField(
        max_length=20, verbose_name="titulo da categoria")
    descricao_categoria = models.CharField(
        max_length=100, verbose_name="descrição da categoria")
    imagem_categoria = models.ImageField(upload_to='images/', null=True)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.titulo_categoria


class Posts(models.Model):
    titulo_post = models.CharField(
        max_length=20, verbose_name="titulo do post")
    sub_titulo = models.CharField(
        max_length=100, verbose_name="subtitulo do post")
    conteudo_post = models.TextField(verbose_name="conteudo do post")
    data_criacao = models.DateTimeField(auto_now=True)
    imagem_post = models.ImageField(upload_to='images/', null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.titulo_post


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='images/', null=True)
    descricao = models.TextField(max_length=400)

    def __str__(self):
        return str(self.user)
