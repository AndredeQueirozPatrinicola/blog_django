from distutils import log
from multiprocessing import context
from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm

#from core.models import Categorias

def index(request):
    return render(request, 'index.html')



def login_page(request):
    return render(request, 'login.html')



def signup(request):
    return render(request, 'signup.html')



def teste(request):
    return render(request, 'post-design.html')



def post(request):
    return render(request, 'post.html')

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
        form = CreateUserForm()
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"Account was created for {user}")
            return redirect("/index/")

        else:
            messages.error(request, "Invalid sign up")
            return redirect('/signup/')
