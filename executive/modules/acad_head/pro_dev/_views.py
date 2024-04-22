from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from executive.modules.acad_head.pro_dev._table import prodev_attendance
from executive.modules.acad_head.pro_dev._json  import professional_development
import json

@login_required(login_url='login')
def pd_asView(request):
    program_counts = professional_development.workshop_data(request)
    program_types  = professional_development.programtype_data(request)
    program_types_total = professional_development.progtypecount_data(request)
    program_types_total_now = professional_development.prodevpresent_data(request)
    programs_distinct_counts = professional_development.programcount_data(request)
    programs_distinct = professional_development.distinctprogram_data(request)
    serialized_program_counts = json.dumps(program_counts)
    serialized_program_types = json.dumps(program_types)
    serialized_pt_total = json.dumps(program_types_total)
    serialized_ptt_now = json.dumps(program_types_total_now)
    serialized_programs_distinct_counts = json.dumps(programs_distinct_counts)
    serialized_program_distinct = json.dumps(programs_distinct)


    state = 'active'
    serialized_state = json.dumps(state)

    context = {
        'prodev_programs': serialized_program_counts,
        'program_types'  : serialized_program_types,
        'program_types_total': serialized_pt_total,
        'program_types_total_now': serialized_ptt_now,
        'program_distinctCounts': serialized_programs_distinct_counts,
        'program_distinct': serialized_program_distinct,
        'requestz': serialized_state,
    }
    return render(request, 'executive/pages/prodev_analytics.html', context)

@login_required(login_url='login')
def pe_asView(request):
    fis_prodev_list = prodev_attendance(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(fis_prodev_list, safe=False)
    else:
        pass