from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
# from executive.models import TableThree

def prdv_wrkshp_att(request):
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     queryset = TableThree.objects.all() 
    #     data = [{
    #             'faculty_no'        : item.faculty_no       ,
    #             'training_title'    : item.training_title   ,
    #             'description'       : item.description      ,
    #             'training_date'     : item.training_date    ,
    #             'training_time'     : item.training_time    ,
    #             'duration'          : item.duration         ,
    #             'location'          : item.location         ,
    #         } for item in queryset]
    #     return JsonResponse(data, safe=False)
    return render(request, 'executive/pages/prodev_attendance.html')


# def prdv_wrkshp_att(request):
#     records = TableTwo.objects.all()
#     data = serialize('json', records)
#     return JsonResponse(data, safe=False)

# def prdv_wrkshp_att(request):
#     records = TableThree.objects.all()
#     data = serialize('json', records)
#     return render(request, 'executive/pages/prodev_attendance.html', {'json_data': data})




# executive/views.py

# from django.http import JsonResponse
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_http_methods
# from executive.models import TableThree

# @login_required(login_url='login')
# @require_http_methods(["GET"])
# def prdv_wrkshp_att(request):
#     queryset = TableThree.objects.all()
#     data = list(queryset.values('faculty_no','training_title','description','training_date','training_time','duration','location'))

#     # return JsonResponse(data, safe=False)
#     return render(request, 'executive/pages/prodev_attendance.html', {'json_data': data})