from django.contrib import admin
from core.models import Categorias, Posts, Person

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_post', 'sub_titulo','autor', 'data_criacao', 'imagem_post', 'categoria')
    list_filter=('titulo_post','autor','data_criacao')

admin.site.register(Posts, PostsAdmin)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id' , 'titulo_categoria', 'imagem_categoria')
    
admin.site.register(Categorias, CategoriasAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'descricao', 'imagem')

admin.site.register(Person, PersonAdmin)