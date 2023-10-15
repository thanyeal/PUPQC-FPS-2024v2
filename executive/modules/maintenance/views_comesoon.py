
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def coming_soon(request):
    return render(request, 'coming_soon/coming_soon.html')
