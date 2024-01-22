from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def fac_mgmnt(request):
    return render(request, 'executive/pages/fac_mgmnt.html')