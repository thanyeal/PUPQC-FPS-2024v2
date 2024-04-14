# from executive.models import TableTwo, TableThree
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from executive.api import api_routes

@login_required(login_url='login')
def prodev_attendance(request):
    fis_prodev = api_routes.get_fis_prodev_data(request)
    fis_prodev_list = []
    
    for prodev_details in fis_prodev:
        program_title = prodev_details['title']
        program_start = prodev_details['date_start']
        program_end   = prodev_details['date_end']
        program_speaker = prodev_details['conducted_by']
        program_type = prodev_details['type']

        fis_prodev_list.append({
            'Program_Title'   : program_title,
            'Program_Start'   : program_start,
            'Program_End'     : program_end,
            'Program_Speaker' : program_speaker,
            'Program_Type'    : program_type
        })
        

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(fis_prodev_list, safe=False)
    else:
        return (fis_prodev_list) 
    

    #     queryset_tabletwo = TableTwo.objects.all()
    #     data_tabletwo = [{
    #         'faculty_no': item.faculty_no,
    #         'training_title': item.training_title,
    #         'description': item.description,
    #         'training_date': item.training_date,
    #         'training_time': item.training_time,
    #         'duration': item.duration,
    #         'location': item.location,
    #     } for item in queryset_tabletwo]

    #     queryset_tablethree = TableThree.objects.all()
    #     data_tablethree = [{
    #         'faculty_name': item.faculty_name,
    #         'time_in': item.time_in,
    #         'time_out': item.time_out,
    #         'training_title': item.training_title,
    #     } for item in queryset_tablethree]

    #     # Combine both table data into a single response
    #     response = {
    #         'table_two_data': data_tabletwo,
    #         'table_three_data': data_tablethree
    #     }

    #     return JsonResponse(response)

    # return render(request, 'executive/pages/prodev_attendance.html')