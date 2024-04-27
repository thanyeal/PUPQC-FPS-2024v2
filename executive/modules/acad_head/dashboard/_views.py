from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from executive.modules.acad_head.dashboard._json import evaluations_data, publications_data, authentications, rpublicatiob_data
from executive.modules.acad_head.pro_dev._json  import professional_development
import json

@login_required(login_url='login')
def db_asView(request):
    program_types = professional_development.programtype_data(request)
    programs_distinct           = professional_development.distinctprogram_data(request)
    program_types_total_now     = professional_development.prodevpresent_data(request)
    programs_distinct_counts    = professional_development.programcount_data(request)
    serialized_high_faculty = evaluations_data(request)
    serialized_grouped_counted, serialized_percentage_data, serialized_response = publications_data(request)
    serialized_first_name  = authentications(request)
    state = 'active'
    serialized_state = json.dumps(state)
    serialized_program_types    = json.dumps(program_types)
    serialized_ptt_now          = json.dumps(program_types_total_now)
    serialized_program_distinct = json.dumps(programs_distinct)
    serialized_pdc              = json.dumps(programs_distinct_counts)

    
    slrzd_rsrch_categories = rpublicatiob_data(request)
    slrzd_grouped_data  = rpublicatiob_data(request)
    slrzd_grouped_counted  = rpublicatiob_data(request)
    slrzd_percentage_data  = rpublicatiob_data(request)
    slrzd_specific_year_data  = rpublicatiob_data(request)
    slrzd_highest_year  = rpublicatiob_data(request)
    slrzd_lowest_year  = rpublicatiob_data(request)
    slrzd_totalresearch  = rpublicatiob_data(request)

    context = {
        'first_name'                : serialized_first_name         ,
        'program_types'             : serialized_program_types,
        'highest_counts'            : serialized_high_faculty       ,
        'total_research_papers'     : serialized_grouped_counted    ,
        'percent_research_papers'   : serialized_percentage_data    ,
        'response_call'             : serialized_response           ,
        'requestz'                  : serialized_state              , 

        
        'js_grouped_counted'    : slrzd_grouped_counted     ,
        'program_distinctCounts': serialized_pdc,
        'program_distinct': serialized_program_distinct,
    }

    return render(request, 'executive/dashboard.html', context)