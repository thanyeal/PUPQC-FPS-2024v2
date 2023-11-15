from django.shortcuts import render

def retention_insights(request):
    return render(request, 'executive/pages/rtnt_insights.html')