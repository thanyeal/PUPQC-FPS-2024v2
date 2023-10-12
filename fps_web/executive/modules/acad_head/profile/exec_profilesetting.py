
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def exec_p_sett(request):
    return render(request, 'profile/exec_p_sett.html')