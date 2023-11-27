from django.shortcuts import render

def awards_analytics(request):
    return render(request, 'executive/pages/awards_analytics.html')