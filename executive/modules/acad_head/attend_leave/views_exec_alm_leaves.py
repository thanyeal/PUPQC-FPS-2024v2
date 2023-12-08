from django.shortcuts import render
from django.http import JsonResponse
from executive.models import TableSix
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def alm_leaves_rec(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableSix.objects.all() 
        data = [{
                "leave_faculty"   : item.leave_faculty,
                "leave_type"      : item.leave_type,
                "leave_start"     : item.leave_start,
                "leave_end"       : item.leave_end,
                "leave_duration"  : item.leave_duration,
                "leave_status"    : item.leave_status,
            } for item in queryset]
        return JsonResponse(data, safe=False)   
    return render(request, 'executive/pages/alm_leaves_rec.html')