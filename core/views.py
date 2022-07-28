from distutils import log
from multiprocessing import context
from urllib import response
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .forms import CreateUserForm
from .models import Categorias, Posts


#Login/Signup controller

def login_page(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def registerUser(request):
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def submit_log_in(request):
    
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



#Render pages, DB Queries

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
    context = {
        'post':post
    }
    return render(request, 'post.html', context)


def show_posts(request, id_categoria):
    post = Posts.objects.filter(categoria=id_categoria)
    context = {
        'post' : post
    }
    return render(request, 'posts.html', context)


def perfil(request, username):
    return render(request, 'perfil.html')


def post_design(request):
    categoria = Categorias.objects.all
    context = {
        'categoria' : categoria
    }

    return render(request, 'post-design.html', context)


def categorie_design(request):
    return render(request, 'categorie-design.html')