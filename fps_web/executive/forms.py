from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )
    last_name = forms.CharField(
        widget=forms.TextInput
    )
    first_name = forms.CharField(
        widget=forms.TextInput
    )
    username = forms.CharField(
        widget=forms.TextInput
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'last_name', 'first_name', 'username']

class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput
    )
    password = forms.CharField(
        widget=forms.PasswordInput
    )

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(
        label='Choose Excel File'
    )
