from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def prdv_wrkshp_anl(request):
    return render(request, 'executive/pages/prodev_analytics.html')