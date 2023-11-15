from django.shortcuts import render

def retention_analytics(request):
    return render(request, 'executive/pages/rtnt_analytics.html')