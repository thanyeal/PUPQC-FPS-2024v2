from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from executive.modules.acad_head.dashboard._json import evaluations_data, publications_data, authentications
from executive.modules.acad_head.pro_dev._json  import professional_development
import json

@login_required(login_url='login')
def db_asView(request):
    program_types = professional_development.programtype_data(request)
    serialized_prctg_rating, serialized_high_faculty = evaluations_data(request)
    serialized_grouped_counted, serialized_percentage_data, serialized_response = publications_data(request)
    serialized_first_name  = authentications(request)
    state = 'active'
    serialized_state = json.dumps(state)
    serialized_program_types    = json.dumps(program_types)

    context = {
        'first_name'                : serialized_first_name         ,
        'program_types'             : serialized_program_types,
        'percentage'                : serialized_prctg_rating       ,
        'highest_counts'            : serialized_high_faculty       ,
        'total_research_papers'     : serialized_grouped_counted    ,
        'percent_research_papers'   : serialized_percentage_data    ,
        'response_call'             : serialized_response           ,
        'requestz'                  : serialized_state              , 
    }

    return render(request, 'executive/dashboard.html', context)