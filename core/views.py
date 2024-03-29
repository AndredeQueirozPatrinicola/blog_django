from collections import UserString
from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .forms import CreateUserForm, EditPerfilForm, SubmitCategoriaForm, SubmitPostForm, UpdateUserForm, UpdateImageForm
from .models import Categorias, Person, Posts
from .utils import auto_login


#Login/Signup controller

def login_page(request):
    return render(request, 'login.html')


@login_required(login_url="/")
def logout_user(request):
    logout(request)
    return redirect('/')


def registerUser(request):
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def submit_log_in(request, **kwargs):
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            
            return redirect('/')
        else:
            messages.error(request, "Invalid user or password")
            return redirect('/login/')
    


def submit_signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"Account was created for {user}")
            return redirect("/signup/")

        else:
            messages.error(request, "Your Username must be unique")
            messages.error(request, "Your password must have at least 8 characters")
            messages.error(request, "Your password must be different from your username")
            return redirect('/signup/')

def index(request):
    categoria = Categorias.objects.all()
    context = {
    'categoria':categoria,
    'image_cap' : "O servidor gratuito do Heroku Apaga a imagem da postagem depois de um tempo"
    }
    return render(request, 'index.html', context)


@login_required(login_url="/")
def post_categoria(request):
    return render(request, 'post-cat.html')    


def post(request, id_post):
    post = Posts.objects.filter(id=id_post)
    conteudo = post.values()[0].get('autor_id')
    autor = User.objects.get(id=conteudo)
    context = {
        'post':post,
        'autor' : autor,
        'image_cap' : "O servidor gratuito do Heroku Apaga a imagem da postagem depois de um tempo"
    }
    return render(request, 'post.html', context)


def show_posts(request, id_categoria):
    post = Posts.objects.filter(categoria=id_categoria)
    context = {
        'post' : post,
        'image_cap' : "O servidor gratuito do Heroku Apaga a imagem da postagem depois de um tempo"
    }
    return render(request, 'posts.html', context)


@login_required(login_url="/")
def perfil(request, id_user):
    user = Person.objects.filter(user=id_user).values('user', 'imagem', 'descricao')    
    context = {}
    return render(request, 'perfil.html', context)


@login_required(login_url="/")
def editar_perfil(request, id_user):
    person = Person.objects.filter(user=id_user).values('user', 'imagem', 'descricao')
    userconf = UpdateUserForm()
    userinfo = EditPerfilForm()
    context = {
        'form1' : userconf,
        'form2' : userinfo,
        'person' : person
    }

    return render(request, 'edit-perfil.html', context)

@login_required(login_url="/")
def submit_edicao(request, id_user):
    try:
        if request.POST:
            user = request.POST.get('user')
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            last_name = request.POST.get('last_name')
            descricao = request.POST.get('descricao')

            usuario = User.objects.filter(id=user)
            if usuario.exists(): 
                verifica_usuario = User.objects.filter(username=username).values('id')
                if verifica_usuario and user != verifica_usuario[0].get('id'):
                    messages.error(request, "O username deve ser unico.")
                    return redirect(f'/perfil/{id_user}/editar-perfil')
                else:
                    usuario.update(id=user,
                                username=username,
                                email=email,
                                first_name=first_name,
                                last_name=last_name)


            person = Person.objects.filter(user=user)
            if person.exists():
                person.update(user=user,
                            descricao=descricao)
            else:
                person.create(user_id=user,descricao=descricao)


        else:
            messages.error(request, "Houve um problema para atualizar as informações")
            return redirect(f'/perfil/{id_user}/editar-perfil')
    
    except:
        messages.error(request, "Algo de errado ")
        return redirect(f'/perfil/{id_user}/editar-perfil')

    return redirect(f'/perfil/{id_user}')

@login_required(login_url="/")
def editar_imagem(request, id_user):
    person = Person.objects.filter(user=id_user).values('imagem')
    form = UpdateImageForm()
    context = {
        'person' : person,
        'form' : form
    }
    return render(request, 'edit-imagem.html', context)

@login_required(login_url="/")
def submit_imagem(request, id_user):
    imagem = request.POST.get('imagem')
    teste = request.FILES
    try:
        person = Person.objects.filter(user=id_user)
        person.update(
                        imagem=imagem
                     )
    except:
        messages.error(request, 'Não foi possivel atualizar a imagem')

    return redirect(f'/perfil/{id_user}/editar-imagem')


@login_required(login_url="/")
def post_design(request):
    categoria = Categorias.objects.all()
    form = SubmitPostForm()

    context = {
        'categoria' : categoria,
        'form' : form
    }

    return render(request, 'design-post-categ.html', context)


@login_required(login_url="/")
def categorie_design(request):
    form = SubmitCategoriaForm()

    context = {
        'form' : form
    }

    return render(request, 'design-post-categ.html', context)


@login_required(login_url="/")
def submit_post(request):
       
    form = SubmitPostForm()

    if request.method == 'POST':

        form = SubmitPostForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            print('validou')
            form.save()


            return redirect(f'/')
        
        else:
            print(form.cleaned_data)
            print('nao ta certo')
            return redirect('/post-design/')


@login_required(login_url="/")
def submit_categoria(request):
   
    form = SubmitCategoriaForm()

    if request.method == 'POST':

        form = SubmitCategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            print('validou')
            form.save()

            return redirect('/')
        
        else:
            print(form.cleaned_data)
            print('nao ta certo')
            return redirect('/categorie-design/')

    return redirect('/')
