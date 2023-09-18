from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url="login")
def exec_dashboard(request):
    return render(request, 'executive/exec_dashboard.html')

def evaluations(request):
    return render(request, 'executive/pages/evaluations.html')