from django.shortcuts import render
from executive.models import User
# from django.contrib.auth.decorators import login_required

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

