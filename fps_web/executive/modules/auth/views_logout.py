
from django.shortcuts import redirect
from django.contrib import messages

def logout(request):
    messages.success(request, 'Successfully logged out')
    return redirect('login')