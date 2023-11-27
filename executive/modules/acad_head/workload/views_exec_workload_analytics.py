from django.shortcuts import render

def workload_analytics(request):
    return render(request, 'executive/pages/workload_analytics.html')