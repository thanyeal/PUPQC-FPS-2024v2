from django.shortcuts import render
from django.http import JsonResponse
from executive.models import TableFive

def mrt_promote(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableFive.objects.all() 
        data = [{
                'merit_faculty_name'        : item.merit_faculty_name ,
                'merit_faculty_status'      : item.merit_faculty_status  ,
                'merit_ave_dept_rate'       : item.merit_ave_dept_rate  ,
                'merit_rsrch_publish'       : item.merit_rsrch_publish  ,
                'merit_training_attended'   : item.merit_training_attended  ,
                'merit_promotion'           : item.merit_promotion  
            } for item in queryset]
        return JsonResponse(data, safe=False)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableFive.objects.all().values('merit_faculty_name', 'merit_faculty_status', 'merit_promotion')
        data = list(queryset)
        return JsonResponse(data, safe=False)
    
    return render(request, 'executive/pages/mrt_promote.html')