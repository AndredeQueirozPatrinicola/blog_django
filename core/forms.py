
from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from core.models import Categorias, Person, Posts, User
from core import models


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'input-login'}),
            'first_name' : forms.TextInput(attrs={'class':'input-login'}),
            'last_name' : forms.TextInput(attrs={'class':'input-login'}),
            'email' : forms.TextInput(attrs={'class':'input-login'}),
            'password1' : forms.PasswordInput(attrs={'class':'input-login'}),
            'password2' : forms.PasswordInput(attrs={'class':'input-login'})
        }


class SubmitCategoriaForm(ModelForm):

    class Meta:
        model = Categorias
        fields = ['titulo_categoria', 'descricao_categoria', 'imagem_categoria']
        widgets = {
            'titulo_categoria': forms.TextInput(attrs={'class':'input-login'}),
            'descricao_categoria' : forms.TextInput(attrs={'class':'input-login'}),
            
        }

class SubmitPostForm(ModelForm):

    class Meta:
        model = Posts
        fields = ['titulo_post', 'sub_titulo', 'conteudo_post','imagem_post', 'categoria', 'autor']
        widgets = {
            'titulo_post' : forms.TextInput(attrs={'class':'input-login'}),
            'sub_titulo' : forms.TextInput(attrs={'class':'input-login'}),
            'conteudo_post' : forms.Textarea(attrs={'class':'post-content-input'}),
            'autor' : forms.Textarea(attrs={'id':'autor', 'value': '', 'type': 'hidden'})
       }
        labels={'autor': ''}


class EditPerfilForm(ModelForm):
    class Meta:
        model = Person
        fields = ['user', 'descricao']
        widgets = {
            'user' : forms.Textarea(attrs={'id':'user'})
        }
        labels = {'user':''}
        

class UpdateUserForm(ModelForm):
    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name']