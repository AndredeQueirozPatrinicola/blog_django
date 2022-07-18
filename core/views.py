from distutils import log
from multiprocessing import context
from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm
from .models import Posts

#from core.models import Categorias

def index(request):
    return render(request, 'index.html')



def login_page(request):
    return render(request, 'login.html')



def post(request):
    post1 = Posts.objects.all()
    context = {
        'post':post1
    }
    return render(request, 'post.html', context)


@login_required(login_url="/")
def post_categoria(request):
    return render(request, 'post-cat.html')    

'''
def categoria(request, id_categoria):
    categoria_id = Categorias.objects.filter(id = id_categoria)
    return response()
'''


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



def logout_user(request):
    logout(request)
    return redirect('/')


def registerUser(request):
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'signup.html', context)



def submit_signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"Account was created for {user}")
            return redirect("/")

        else:
            messages.error(request, "Your Username must be unique")
            messages.error(request, "Your password must have at least 8 characters")
            messages.error(request, "Your password must be different from your username")
            return redirect('/signup/')
