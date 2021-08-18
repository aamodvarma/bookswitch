from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




#
#class LoginForm(UserCreationForm):
#    class Meta:
#        model = User
#        email = forms.EmailField()
#        fields = ['username','email', 'first_name', 'password1', 'password2']
#
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'password1', 'password2')
