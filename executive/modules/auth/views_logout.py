from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def custom_logout(request):
    logout(request)
    # Redirect to the login page after logout
    return redirect(reverse('login'))
