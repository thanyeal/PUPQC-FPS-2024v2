from django.shortcuts import render
from django.http import JsonResponse
from executive.models import TableSeven
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def workload_dat(request):
    # Check if it's an AJAX request and return JSON data
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableSeven.objects.all() 
        data = [{
                'workload_faculty'  : item.workload_faculty ,
                'workload_semester' : item.workload_semester,
                'workload_course'   : item.workload_course  ,
                'workload_types'    : item.workload_types   ,
                'workload_duties'   : item.workload_duties  ,
                'workload_total'    : item.workload_total   ,
            } for item in queryset]
        return JsonResponse(data, safe=False)
    return render(request, 'executive/pages/workload_recs.html')