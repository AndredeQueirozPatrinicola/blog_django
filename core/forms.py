from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



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

