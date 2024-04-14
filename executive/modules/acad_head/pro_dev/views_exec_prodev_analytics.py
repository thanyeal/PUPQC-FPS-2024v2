from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from collections import Counter
import json

from django.http import JsonResponse
from executive.modules.acad_head.pro_dev.views_exec_prodev import prodev_attendance
from executive.modules.acad_head.pro_dev.views_exec_prodev_program_types import prodev_program_type, prodev_program_type_count, prodev_program_type_count_present_year



@login_required(login_url='login')
def prdv_wrkshp_anl(request):

    prodev_table = prodev_attendance(request)
    current_year = datetime.now().year
    past_two_years = [current_year - i for i in range(10)]
    program_counts = Counter()
    for entry in prodev_table:
        date_end = datetime.strptime(entry['Program_End'], '%a, %d %b %Y %H:%M:%S %Z')
        year = date_end.year
        if year in past_two_years:
            program_counts[year] += 1
    serialized_program_counts = json.dumps(program_counts)



    program_types = prodev_program_type(request)
    serialized_program_types = json.dumps(program_types)


    program_types_total = prodev_program_type_count(request)
    serialized_pt_total = json.dumps(program_types_total)


    program_types_total_now = prodev_program_type_count_present_year(request)
    serialized_ptt_now = json.dumps(program_types_total_now)


    state = 'active'
    serialized_state = json.dumps(state)

    context = {
        'prodev_programs': serialized_program_counts,
        'program_types'  : serialized_program_types,
        'program_types_total': serialized_pt_total,
        'program_types_total_now': serialized_ptt_now,
        'requestz': serialized_state,
    }

    # return JsonResponse(context, safe=False)
    return render(request, 'executive/pages/prodev_analytics.html', context)