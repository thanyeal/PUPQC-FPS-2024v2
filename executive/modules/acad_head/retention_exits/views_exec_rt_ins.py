from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def retention_insights(request):
    return render(request, 'executive/pages/rtnt_insights.html')