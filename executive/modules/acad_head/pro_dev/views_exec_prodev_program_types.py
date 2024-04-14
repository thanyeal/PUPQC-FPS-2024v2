from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from executive.modules.acad_head.pro_dev.views_exec_prodev import prodev_attendance
import json
from datetime import datetime

@login_required(login_url='login')
def prodev_program_type(request):
    fis_prodev_list = prodev_attendance(request)
    type_counts = {}
    for program_details in fis_prodev_list:
        end_date = datetime.strptime(program_details['Program_End'], "%a, %d %b %Y %H:%M:%S %Z")
        year = end_date.year
        program_type = program_details['Program_Type'].lower() 
        if year not in type_counts:
            type_counts[year] = {}
        type_counts[year][program_type] = type_counts[year].get(program_type, 0) + 1
    return (type_counts)


@login_required(login_url='login')
def prodev_program_type_count(request):
    fis_prodev_list = prodev_attendance(request)
    total_program_types = {} # not called
    total_count = 0

    for program in fis_prodev_list:
        program_type = program['Program_Type']
        total_program_types[program_type] = total_program_types.get(program_type, 0) + 1
        total_count += 1

    return (total_count)

def prodev_program_type_count_present_year(request):
    fis_prodev_list = prodev_attendance(request)
    present_year = datetime.now().year
    total_count_present_year = 0
    program_types_present_year = {} # not called

    for program in fis_prodev_list:
        program_year = datetime.strptime(program['Program_End'], "%a, %d %b %Y %H:%M:%S %Z").year
        if program_year == present_year:
            program_type = program['Program_Type']
            program_types_present_year[program_type] = program_types_present_year.get(program_type, 0) + 1
            total_count_present_year += 1

    return (total_count_present_year)