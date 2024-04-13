
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import json, requests
from datetime import date
from executive.api import api_routes
from django.http import JsonResponse
from executive.modules.acad_head.evaluations.views_exec_evalupload import evaluations

@login_required(login_url='login')
def exec_dashboard(request):

    json_responsetwo = evaluations(request)
    ris_api_data = api_routes.get_ris_api(request)


    # Faculty Info System
    rating_above_3 = [item for item in json_responsetwo if float(item['student_ave']) > 4.00]
    rating_below_3 = [item for item in json_responsetwo if float(item['student_ave']) <= 3.99]
    count_ra3 = len(rating_above_3)
    count_rb3 = len(rating_below_3)
    total_rec = len(json_responsetwo)
    pctg_ra3 = (count_ra3 / total_rec) * 100
    pctg_rb3 = (count_rb3 / total_rec) * 100
    pctg_ra3 = round(pctg_ra3, 2)
    pctg_rb3 = round(pctg_rb3, 2)
    two_ratings = {
        'pctg_ra3': pctg_ra3    ,
        'pctg_rb3': pctg_rb3    ,
        'count_ra3': count_ra3  ,
        'count_rb3': count_rb3
    }
    serialized_prctg_rating  = json.dumps(two_ratings)


    # Research Info System
    if ris_api_data:
        think_response = 1
        totalresearch = len(ris_api_data)
        grouped_counted = {}
        total_count = 50
        for item in ris_api_data:
            if 'Publication Year' in item and item['Publication Year'] and isinstance(item['Publication Year'], str):
                year = int(item['Publication Year'][:4])
                grouped_counted.setdefault(year, {'count': 0})['count'] += 1
        percentage_data = {}
        for year, count in grouped_counted.items():
            percentage_data[year] = {'percentage': (count['count'] / total_count * 100)}
        serialized_grouped_counted = json.dumps(totalresearch)
        serialized_percentage_data = json.dumps(percentage_data)
        serialized_response = json.dumps(think_response)
    else:
        think_response = 0
        totalresearch = 0
        percentage_data = {'percentage': 0}
        serialized_grouped_counted = json.dumps(totalresearch)
        serialized_percentage_data = json.dumps(percentage_data)
        serialized_response = json.dumps(think_response)


    # Account User Information
    if request.user.is_authenticated:
        first_name = request.user.first_name
        # custom_data = User.objects.filter(first_name=first_name)  
    else:   
        first_name = "" 

    serialized_first_name = json.dumps(first_name)

    state = 'active'
    serialized_state = json.dumps(state)

    context = {
        'total_research_papers'     : serialized_grouped_counted ,
        'percent_research_papers'   : serialized_percentage_data ,
        'first_name'    : serialized_first_name     ,
        'percentage'    : serialized_prctg_rating   ,
        'response_call' : serialized_response       ,
        'requestz': serialized_state, 
    }
    return render(request, 'executive/exec_dashboard.html', context)
