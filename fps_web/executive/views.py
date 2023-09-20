from django.shortcuts import render, redirect
from django.views import View
from executive.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from .forms import CustomRegistrationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required


# ! ++++++++++++++++++++++++++  for authentication views  ++++++++++++++++++++++++++++++ #

class RegistryView(View):
    def get(self, request):
        form = CustomRegistrationForm()
        return render(request, 'registration/registry.html', {'form': form})

    def post(self, request):
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user to the database with hashed password
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.save()
            login(request, user)
            
            messages.success(request, 'Successfully registered!')
            return redirect('exec_dashboard')
        else:
            messages.error(request, 'Registration failed. Please check the form for errors.')
            return render(request, 'registration/registry.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = CustomLoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    login(request, user)
                    messages.success(request, 'Successfully logged in!')
                    return redirect('exec_dashboard')
                else:
                    messages.error(request, 'Invalid credentials')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist')
        else:
            messages.error(request, 'Invalid form submission')
        return render(request, 'registration/login.html', {'form': form})

class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, 'Successfully logged out')
        return redirect('login')

# ! ++++++++++++++++++++++++++  for main pages views  ++++++++++++++++++++++++++++++ #

# @login_required
def exec_dashboard(request):
    current_user = request.user
    context = {
        'current_user': current_user,
    }   
    return render(request, 'executive/exec_dashboard.html', context)

# @login_required
def evaluations(request):
    current_user = request.user
    context = {
        'current_user': current_user,
    }   
    return render(request, 'executive/pages/evaluations.html', context)

# for in development page
def coming_soon(request):
    return render(request, 'coming_soon/coming_soon.html')

# // ++++++++++++++++++++++++++  for  something  views  ++++++++++++++++++++++++++++++ #


