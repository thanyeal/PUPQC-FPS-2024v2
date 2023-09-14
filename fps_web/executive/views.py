from django.shortcuts import render

# Create your views here.

def exec_dashboard(request):
    return render(request, 'executive/exec_dashboard.html')

def evaluations(request):
    return render(request, 'executive/pages/evaluations.html')