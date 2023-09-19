from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from executive.models import User

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password2'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    middlename = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Middlename'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'lastname', 'firstname', 'middlename']

class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
    class Meta:
        model = User
        fields = ['email', 'password']