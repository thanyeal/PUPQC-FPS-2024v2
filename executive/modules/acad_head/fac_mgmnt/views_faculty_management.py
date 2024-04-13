from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from executive.api import api_routes
from executive.modules.acad_head.fac_mgmnt.views_faculty_rep import faculty_indiv_report
from executive.modules.acad_head.fac_mgmnt.views_faculty_inf_route import faculty_info_route
from executive.modules.acad_head.evaluations.views_exec_evalupload import evaluations
import json, requests

@login_required(login_url='login')
def fac_mgmnt(request):
    
    fis_api_data = faculty_indiv_report(request)
    ris_api_data = api_routes.get_ris_api(request)
    fis_overalls = evaluations(request)
    fis_informat = faculty_info_route(request)

    semesters = ['First', 'Second'] 
    faculty_name = None     


    if request.method == 'POST':
        faculty_name_from_ajax = request.POST.get('faculty_name')
        faculty_name = faculty_name_from_ajax[:10].upper()
        faculty_name_in_logic = faculty_name

        average_categories = {}
        for semester in semesters:
            semester_data = [
                entry for entry in fis_api_data if entry.get('semester') == semester and
                entry.get('name')[:10].upper() == faculty_name_in_logic #and
                # entry.get('Year', '').startswith(str(present_date))
            ]
            if semester_data:
                avg_spvs_rating = round(sum(float(entry['acad_head_calc_percentage']) for entry in semester_data) / len(semester_data), 1)
                avg_stud_rating = round(sum(float(entry['student_calc_percentage'  ]) for entry in semester_data) / len(semester_data), 1)
                avg_dirc_rating = round(sum(float(entry['director_calc_percentage' ]) for entry in semester_data) / len(semester_data), 1)
                avg_self_rating = round(sum(float(entry['self_calc_percentage'     ]) for entry in semester_data) / len(semester_data), 1)
                average_categories.update({
                    f'Supervisor_{semester}': [avg_spvs_rating],
                    f'Student_{semester}'   : [avg_stud_rating],
                    f'Director_{semester}'  : [avg_dirc_rating],
                    f'Self_{semester}'      : [avg_self_rating],
                })

        research_counted = {}
        for item in ris_api_data:
            if faculty_name in item.get('Author').upper():
                year = item.get('Publication Year')[:4]
                research_counted.setdefault(year, {'count': 0})['count'] += 1

        overall_ratings = {}
        for faculty in fis_overalls:
            if faculty_name in faculty.get('Name')[:10].upper():
                academic_year = str(faculty['school_year'][:9])

                overall_ratings.setdefault(academic_year, {})
                for sem in semesters:
                    overall_ratings[academic_year][sem.lower() + '_sem_rating'] = {
                        'acadhead_rating' : faculty['acad_head_ave'],
                        'individs_rating' : faculty['self_ave'],
                        'director_rating' : faculty['director_ave'], 
                        'students_rating' : faculty['student_ave'],
                    }

        indiv_information = {}
        for individual in fis_informat:
            if faculty_name == individual.get('Faculty_name')[:10].upper():
                indiv_information = {
                    'faculty_name': individual.get('Faculty_name'),
                    'faculty_type': individual.get('Faculty_type'),
                    'faculty_rank': individual.get('Faculty_rank'),
                    'faculty_addr': individual.get('Faculty_addr'),
                    'faculty_mail': individual.get('Faculty_mail'),
                    'faculty_numb': individual.get('Faculty_numb'),
                    'faculty_degr': individual.get('Faculty_degr'),
                }

        faculty_progress = {}
        for progresses in fis_api_data:
            if faculty_name in progresses.get('name')[:10].upper():
                general_rating = progresses.get('general_rating')
                rounded_rating = round(general_rating, 2)
                partial_percentage = min(rounded_rating / 5 * 100, 100)
                final_percentage = round(partial_percentage, 2)
                faculty_progress.update({
                    'overall_percent': final_percentage
                })

        return JsonResponse({
            'faculty_mgmt'          : average_categories,
            'publication_counts'    : research_counted,
            'overall'               : overall_ratings,
            'the_faculty'           : indiv_information,
            'the_progress'          : faculty_progress,

        })

    
    else:
        state = 'active'
        serialized_state = json.dumps(state)
        context = {
            'requestz': serialized_state,
        }
        return render(request, 'executive/pages/fac_mgmnt.html', context)
    

# specific_year = 2021  # Replace with the desired year
# present_date = date(specific_year, 1, 1).year
# present_date = date.today().year
# from datetime import date
# import os, requests, json, datetime
# API for Research Information System