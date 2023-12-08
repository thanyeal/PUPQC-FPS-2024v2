from django.shortcuts import render
from django.http import JsonResponse
from executive.models import TableFour
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def rsrch_tracking(request):
    # Check if it's an AJAX request and return JSON data
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableFour.objects.all() 
        data = [{
                'rsrch_author'      : item.rsrch_author     ,
                'rsrch_title'       : item.rsrch_title      ,
                'rsrch_year'        : item.rsrch_year       ,
                'rsrch_publisher'   : item.rsrch_publisher  ,
            } for item in queryset]
        return JsonResponse(data, safe=False)
    return render(request, 'executive/pages/rsrch_tracking.html')