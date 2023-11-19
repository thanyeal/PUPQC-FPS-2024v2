from django.shortcuts import render

def mrt_analytics(request):
    return render(request, 'executive/pages/mrt_analytics.html')