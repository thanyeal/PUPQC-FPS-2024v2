from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from decimal import Decimal
import json
import datetime
from executive.api import api_routes

@login_required(login_url='login')
def convert_decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

@login_required(login_url='login')
def eval_analytics(request):
    # responsez = testfacultyinfodata(request)
    # api_data = responsez.data
    
    fis_api_data = api_routes.get_fis_eval_api(request)
    grouped_data = {}

    for item in fis_api_data:
        eval_year = item['Year']
        year = eval_year[:4]
        semester = item['Semester']

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

        grouped_data[year][semester]['avgz_spvs_rating'].append(item['Supervisor Rating'])
        grouped_data[year][semester]['avgz_stud_rating'].append(item['Students Rating'])
        grouped_data[year][semester]['avgz_peer_rating'].append(item['Peer Rating'])
        grouped_data[year][semester]['avgz_self_rating'].append(item['Self Rating'])

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

# ============================================================================================
#     percent_grpbyyear_persem = {}
#     for year, year_data in grouped_data.items():
#         overall_avg_for_year = {}
#         for semester, semester_data in year_data.items():
#             overall_avg_for_semester = (
#                 float(semester_data['Supervisor Rating']) +
#                 float(semester_data['Students Rating']) +
#                 float(semester_data['Peer Rating']) +
#                 float(semester_data['Self Rating'])
#             ) / 4

#             overall_avg_for_semester = round(overall_avg_for_semester, 3)
#             overall_avg_for_semester_percentage = (overall_avg_for_semester / 5) * 100
#             overall_avg_for_semester_percentage = round(overall_avg_for_semester_percentage, 0)

#             overall_avg_for_year[semester] = overall_avg_for_semester_percentage

#         percent_grpbyyear_persem[year] = overall_avg_for_year

# # ============================================================================================
    current_year = datetime.datetime.now().year
    current_year_data = grouped_data[str(current_year)]
    overall_avg_dict = {}  # Initialize the dictionary
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
            overall_avg_first_percentage = overall_avg_dict.get('overall_avg_first', 0)
            overall_avg_second_percentage = overall_avg_dict.get('overall_avg_second', 0)
# # ============================================================================================
    student_rate_data = {}
    for item in fis_api_data:  # Process all items in the API data
        eval_year = item['Year']
        year = eval_year[:4]
        semester = item['Semester']  # Get the semester for each item

        if year not in grouped_data:
            grouped_data[year] = {
                'First': {
                    'avg_stud_rating': []
                },
                'Second': {
                    'avg_stud_rating': []
                },
                'Summer': {
                    'avg_stud_rating': []
                },
            }
        
        # grouped_data[year][semester]['avg_stud_rating'].append(item['Students Rating'])
        
        if year not in student_rate_data:
            student_rate_data[year] = {}  # Create an empty dictionary for each year

        if semester not in student_rate_data[year]:
            student_rate_data[year][semester] = {
                'Students Rating': []
            }

        # Append ratings to the corresponding semester group
        student_rate_data[year][semester]['Students Rating'].append(item['Students Rating'])

    # Calculate averages for each semester group
    for year, year_data in student_rate_data.items():
        for semester, semester_data in year_data.items():
            semester_data['Students Rating'] = round(sum(float(rating) for rating in semester_data['Students Rating'])/ len(semester_data['Students Rating']),1)
# # ============================================================================================

    rating_above_3 = [item for item in fis_api_data if float(item['Students Rating']) > 4.00]
    rating_below_3 = [item for item in fis_api_data if float(item['Students Rating']) <= 3.99]

    count_ra3 = len(rating_above_3)
    count_rb3 = len(rating_below_3)

    total_rec = len(fis_api_data)

    pctg_ra3 = (count_ra3 / total_rec) * 100
    pctg_rb3 = (count_rb3 / total_rec) * 100

    pctg_ra3 = round(pctg_ra3, 2)
    pctg_rb3 = round(pctg_rb3, 2)

    two_ratings = {
        'pctg_ra3': pctg_ra3,
        'pctg_rb3': pctg_rb3,
        'count_ra3': count_ra3,
        'count_rb3': count_rb3
    }
    
    serialized_data_two      = json.dumps(ave_per_cattz)
    serialized_overall_avg   = json.dumps(overall_avg_dict)
    # serialized_combined_data = json.dumps(student_rate_data)
    serialized_prctg_rating  = json.dumps(two_ratings)

    context = {
        'chart_data_two' : serialized_data_two,
        'overall_avg_data': serialized_overall_avg,
        # 'combined_data': serialized_combined_data,
        'percentage' : serialized_prctg_rating
    }
    #return JsonResponse(context, safe=False)
    return render(request, 'executive/pages/eval_analytics.html', context)
    
    # return render(request, 'executive/pages/eval_analytics.html', context)


