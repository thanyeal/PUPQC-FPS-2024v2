from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from executive.modules.acad_head.evaluates._json      import evaluations_module
from executive.modules.acad_head.evaluates._tables    import evaluations_table
import json

@login_required(login_url='login')
def el_asView(request):
    state = 'active'
    serialized_state         = json.dumps(state)
    serialized_data_two, serialized_overall_avg = evaluations_module.evaluations_data(request)
    serialized_prctg_rating = evaluations_module.countandrating_data(request)
    context = {
            'chart_data_two'    : serialized_data_two       ,
            'overall_avg_data'  : serialized_overall_avg    ,
            'percentage'        : serialized_prctg_rating   ,
            'requestz': serialized_state
        }
    return render(request, 'executive/pages/eval_analytics.html', context)

@login_required(login_url='login')
def em_asView(request):
    result_list = evaluations_table(request)
    return JsonResponse(result_list, safe=False)
