from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def pr_asView(request):
    return render(request, 'executive/pages/performance_ranking.html')