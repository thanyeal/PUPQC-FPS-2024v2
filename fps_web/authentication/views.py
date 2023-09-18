from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from executive.models import User
from validate_email import validate_email
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout

class RegistryView(View):
    def get(self, request):
        return render(request, 'authentication/registry.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            # return JsonResponse({'error': 'Email and password are required'}, status=400)
            messages.error(request, 'Email and Password are required')
            return redirect('registry')
        else:
            hashed_password = make_password(password)
            user = User(email=email, password=hashed_password) 
            user.save()
            messages.success(request, 'Successfully registered!')
            return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        email = request.POST.get('webmail')
        password = request.POST.get('webpass')

        if User.objects.filter(email=email).exists():

            user = User.objects.get(email=email)
            if check_password(password, user.password):
                authenticate(user)
                login(request, user)
                return render(request, 'executive/exec_dashboard.html')
                # messages.success(request, 'Successfully registered!')
                # return JsonResponse({'success': 'Authentication successful'}, status=200)
            else:
                # return JsonResponse({'error': 'Authentication failed'}, status=400)
                messages.error(request, "Credentials doesn't match")
                return redirect('login')
        else:
            User.DoesNotExist
            # return JsonResponse({'error': 'Credentials is not existing' + email}, status=400)
            messages.error(request, 'Credentials is not existing')
            return redirect('login')

class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, 'Successfully logged out')