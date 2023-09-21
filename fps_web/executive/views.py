from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
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
            user = form.save()
            login(request, user)
            
            messages.success(request, 'Successfully registered!')
            return redirect('exec_dashboard')
        else:
            messages.error(request, 'Registration failed. Please check the form for errors.')
            return render(request, 'registration/registry.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = CustomRegistrationForm(data=request.POST)
        return render(request, 'registration/login.html', {'form': form})
    
    # def post(self, request):
    #     form = CustomLoginForm(data=request.POST)

    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')
    #         print(f"Email: {email}, Password: {password}")

    #         user = authenticate(email=email, password=password)
    #         print(user)

    #         if user is not None:
    #             login(request, user)
    #             messages.success(request, 'Successfully logged in!')
    #             return redirect('exec_dashboard')
    #         else:
    #             messages.error(request, 'Invalid credentials')
                
                
    #     else:
    #         messages.error(request, 'Invalid form submission')
    #     return render(request, 'registration/login.html', {'form': form})


# class LoginView(View):
#     def get(self, request):
#         form = CustomLoginForm()
#         return render(request, 'registration/login.html', {'form': form})

#     def post(self, request):
#         form = CustomLoginForm(data=request.POST)
#         if form.is_valid():
#             Email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             print(f"Email: {Email}, Password: {password}")

#             if Email and password is not None:
#                 check_password(password, password)
#                 user = User.objects.get(email=Email)
#                 authenticate(user)
#                 login(request, user)
#                 messages.success(request, 'Successfully logged in!')
#                 return redirect('exec_dashboard')
#             else:
#                 messages.error(request, 'Invalid credentials')
#                 print(user)
#         else:
#             messages.error(request, 'Invalid form submission')
#         return render(request, 'registration/login.html', {'form': form})

def logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('login')

# ! ++++++++++++++++++++++++++  for main pages views  ++++++++++++++++++++++++++++++ #

@login_required(login_url='login')
def exec_dashboard(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        custom_data = User.objects.filter(first_name='first_name')  # Replace with your query
    else:
        first_name = "" 
        custom_data = []
    return render(request, 'executive/exec_dashboard.html', {'first_name': first_name, 'custom_data': custom_data})

@login_required(login_url='login')
def evaluations(request):
    return render(request, 'executive/pages/evaluations.html')

# for in development page
@login_required(login_url='login')
def coming_soon(request):
    return render(request, 'coming_soon/coming_soon.html')

# // ++++++++++++++++++++++++++  for  something  views  ++++++++++++++++++++++++++++++ #


