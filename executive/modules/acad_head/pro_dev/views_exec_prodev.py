from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from executive.models import TableTwo, TableThree
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def prdv_wrkshp_att(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset_tabletwo = TableTwo.objects.all()
        data_tabletwo = [{
            'faculty_no': item.faculty_no,
            'training_title': item.training_title,
            'description': item.description,
            'training_date': item.training_date,
            'training_time': item.training_time,
            'duration': item.duration,
            'location': item.location,
        } for item in queryset_tabletwo]

        queryset_tablethree = TableThree.objects.all()
        data_tablethree = [{
            'faculty_name': item.faculty_name,
            'time_in': item.time_in,
            'time_out': item.time_out,
            'training_title': item.training_title,
        } for item in queryset_tablethree]

        # Combine both table data into a single response
        response = {
            'table_two_data': data_tabletwo,
            'table_three_data': data_tablethree
        }

        return JsonResponse(response)

    return render(request, 'executive/pages/prodev_attendance.html')