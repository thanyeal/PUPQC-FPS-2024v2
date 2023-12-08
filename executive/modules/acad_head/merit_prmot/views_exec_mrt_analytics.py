from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def mrt_analytics(request):
    return render(request, 'executive/pages/mrt_analytics.html')