from django.shortcuts import render

def fac_contents(request):
    return render(request, 'executive/pages/fac_contents.html')