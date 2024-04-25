from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from executive.utils import obfuscate
from executive.modules.acad_head.faculties._json    import faculty_management
from executive.modules.acad_head.faculties._table   import faculty_management_table
from executive.modules.acad_head.faculties._export  import faculty_management_report
from django.shortcuts import render
import json

@login_required(login_url='login')
def fm_asView(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz': serialized_state,
    }
    return render(request, 'executive/pages/faculties.html', context)

@login_required(login_url='login')
def fn_asView(request):
    average_categories = faculty_management.categories_data (request)
    research_counted   = faculty_management.publication_data(request)
    overall_ratings    = faculty_management.overallrate_data(request)
    indiv_information  = faculty_management.facultyinfo_data(request)
    faculty_progress   = faculty_management.progressbar_data(request)
    return JsonResponse({
        'faculty_mgmt'          :   average_categories    ,
        'publication_counts'    :   research_counted      ,
        'overall'               :   overall_ratings       ,
        'the_faculty'           :   indiv_information     ,
        'the_progress'          :   faculty_progress      ,
    })

@login_required(login_url='login')
def fo_asView(request):
    faculty_list = faculty_management_table(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        minified_data = json.dumps(faculty_list, separators=(',', ':'))
        obfuscated_data = obfuscate(minified_data)
        return JsonResponse({'x': obfuscated_data})
    else:
        pass

@login_required(login_url='login')
def fp_asView(request):
    response = faculty_management_report(request)
    if request.method == 'POST':
        response = response
        return response
    else:
        return HttpResponse("Method Not Allowed", status=405)
