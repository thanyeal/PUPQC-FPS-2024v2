from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from decimal import Decimal
import json
import datetime
from django.http import JsonResponse
from executive.api import api_routes
from executive.modules.acad_head.evaluations.views_exec_evalupload import evaluations

@login_required(login_url='login')
def convert_decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

@login_required(login_url='login')
def eval_analytics(request):
    # fis_api_data = api_routes.get_fis_eval_api(request)
    json_response = evaluations(request)

# # ============================================================================================
    # Faculty Evaluation Average Ratings & Trends in Teaching Effectiveness Over Time 
    grouped_data = {}   
    for item in json_response:
        eval_year = item['school_year']
        year = eval_year[:4]
        semester = item['semester']

        if year not in grouped_data:
            grouped_data[year] = {
                'First': {
                    'avgz_spvs_rating': [],
                    'avgz_stud_rating': [],
                    'avgz_peer_rating': [],
                    'avgz_self_rating': []
                },
                'Second': {
                    'avgz_spvs_rating': [],
                    'avgz_stud_rating': [],
                    'avgz_peer_rating': [],
                    'avgz_self_rating': []
                },
                'Summer': {
                    'avgz_spvs_rating': [],
                    'avgz_stud_rating': [],
                    'avgz_peer_rating': [],
                    'avgz_self_rating': []
                }
            }

        grouped_data[year][semester]['avgz_spvs_rating'].append(item['acad_head_ave'])
        grouped_data[year][semester]['avgz_stud_rating'].append(item['student_ave'])
        grouped_data[year][semester]['avgz_peer_rating'].append(item['director_ave'])
        grouped_data[year][semester]['avgz_self_rating'].append(item['self_ave'])

    for year, year_data in grouped_data.items():
        for semester, semester_data in year_data.items():
            for rating_type, ratings in semester_data.items():
                if len(ratings) > 0:
                    semester_data[rating_type] = round(sum(float(rating) for rating in ratings) / len(ratings), 1)
                else:
                    semester_data[rating_type] = 0.0
    ave_per_cattz = [
        {
            'year': year,
            'frst_semester_avg': year_data['First'],
            'scnd_semester_avg': year_data['Second'],
            'summer_semester_avg': year_data['Summer']
        }
        for year, year_data in grouped_data.items()
    ]
    ave_per_cattz.sort(key=lambda x: x['year'])

# # ============================================================================================
    # Faculty Evaluation Average Rating Per Percentage (Current Year Data)
    percent_grpbyyear_persem = {}
    for year, year_data in grouped_data.items():
        overall_avg_for_year = {}
        for semester, semester_data in year_data.items():
            overall_avg_for_semester = (
                float(semester_data['avgz_spvs_rating']) +
                float(semester_data['avgz_stud_rating']) +
                float(semester_data['avgz_peer_rating']) +
                float(semester_data['avgz_self_rating'])
            ) / 4

            overall_avg_for_semester            = round(overall_avg_for_semester, 3)
            overall_avg_for_semester_percentage = (overall_avg_for_semester / 5) * 100
            overall_avg_for_semester_percentage = round(overall_avg_for_semester_percentage, 0)
            overall_avg_for_year[semester]      = overall_avg_for_semester_percentage

        percent_grpbyyear_persem[year] = overall_avg_for_year

# # ============================================================================================
    
    current_year = datetime.datetime.now().year
    terminal_year = current_year - 1
    current_year_data = grouped_data[str(terminal_year)]
    
    overall_avg_dict = {}
    for semester, semester_data in current_year_data.items():
        if semester in ['First', 'Second']: 
            overall_avg_for_semester = (
                float(semester_data['avgz_spvs_rating']) +
                float(semester_data['avgz_stud_rating']) +
                float(semester_data['avgz_peer_rating']) +
                float(semester_data['avgz_self_rating'])
            ) / 4

            overall_avg_for_semester = round(overall_avg_for_semester, 3)
            overall_avg_percentage = (overall_avg_for_semester / 5) * 100
            overall_avg_percentage = round(overall_avg_percentage, 0)

            key_name = f"overall_avg_{semester.lower()}"
            overall_avg_dict[key_name] = overall_avg_percentage

# # ============================================================================================

    # Average Student Scores for Each Faculty 
    rating_above_3 = [item for item in json_response if float(item['student_ave']) > 4.00]
    rating_below_3 = [item for item in json_response if float(item['student_ave']) <= 3.99]

    # Average Student Scores for Each Faculty (Number Counts)
    count_ra3 = len(rating_above_3)
    count_rb3 = len(rating_below_3)

    total_rec = len(json_response)

    # Average Student Scores for Each Faculty (Pie Graph Data)
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
    
    state = 'active'
    serialized_state         = json.dumps(state)
    serialized_data_two      = json.dumps(ave_per_cattz)
    serialized_overall_avg   = json.dumps(overall_avg_dict)
    serialized_prctg_rating  = json.dumps(two_ratings)
    serialized_persem        = json.dumps(percent_grpbyyear_persem)

    context = {
        'chart_data_two'    : serialized_data_two       ,
        'overall_avg_data'  : serialized_overall_avg    ,
        'combined_data'     : serialized_persem         ,
        'percentage'        : serialized_prctg_rating,
        'requestz': serialized_state
    }
    #return JsonResponse(context, safe=False)
    return render(request, 'executive/pages/eval_analytics.html', context)