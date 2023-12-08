from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def fac_analytics(request):
    return render(request, 'executive/pages/fac_analytics.html')