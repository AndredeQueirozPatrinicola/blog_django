from multiprocessing import context
import re
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .forms import CreateUserForm, EditPerfilForm, SubmitCategoriaForm, SubmitPostForm
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
    'categoria':categoria
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
        'autor' : autor
    }
    return render(request, 'post.html', context)


def show_posts(request, id_categoria):
    post = Posts.objects.filter(categoria=id_categoria)
    context = {
        'post' : post
    }
    return render(request, 'posts.html', context)


@login_required(login_url="/")
def perfil(request, id_user):
    user = Person.objects.filter(user=id_user).values('user', 'imagem', 'descricao')    
    context = {}
    return render(request, 'perfil.html', context)


@login_required(login_url="/")
def editar_perfil(request, id_user):
    userconf = User.objects.filter(id=id_user).values('username', 'first_name', 'last_name')
    userinfo = Person.objects.filter(user=id_user).values('user', 'imagem', 'descricao')
    context = {
        'userconf' : userconf,
        'userinfo' : userinfo
    }

    return render(request, 'edit-perfil.html', context)

@login_required(login_url="/")
def submit_edicao(request, id_user):

    


    return redirect(f'/perfil/{id_user}')


@login_required(login_url="/")
def post_design(request):
    categoria = Categorias.objects.all
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
