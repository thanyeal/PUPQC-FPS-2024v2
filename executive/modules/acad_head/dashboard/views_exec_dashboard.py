
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from executive.models import TableOne
from django.db.models import Avg
import json, os, requests
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from datetime import date

@login_required(login_url='login')
def exec_dashboard(request):
    present_date = date.today().year

    if not TableOne.objects.exists():
        return redirect('error_page_404')
    else:
        first_semester_data = TableOne.objects.filter(semester='First', eval_year__year=present_date).order_by('semester', 'eval_year')
        first_semester_avg = first_semester_data.aggregate(
            avgz_spvs_rating=Avg('spvs_rating'),
            avgz_stud_rating=Avg('stud_rating'),
            avgz_peer_rating=Avg('peer_rating'),
            avgz_self_rating=Avg('self_rating') 
        )

        second_semester_data = TableOne.objects.filter(semester='Second', eval_year__year=present_date).order_by('semester', 'eval_year')
        second_semester_avg = second_semester_data.aggregate(
            avgz_spvs_rating=Avg('spvs_rating'),
            avgz_stud_rating=Avg('stud_rating'),
            avgz_peer_rating=Avg('peer_rating'),
            avgz_self_rating=Avg('self_rating')
        )

        summer_semester_data = TableOne.objects.filter(semester='Summer', eval_year__year=present_date).order_by('semester', 'eval_year')
        summer_semester_avg = summer_semester_data.aggregate(
            avgz_spvs_rating=Avg('spvs_rating'),
            avgz_stud_rating=Avg('stud_rating'),
            avgz_peer_rating=Avg('peer_rating'),
            avgz_self_rating=Avg('self_rating')
        )

        ave_per_catt = {
            'spvs_first':   [round ( float ( first_semester_avg  ['avgz_spvs_rating'] ), 1)],
            'stud_first':   [round ( float ( first_semester_avg  ['avgz_stud_rating'] ), 1)],
            'peerr_first':  [round ( float ( first_semester_avg  ['avgz_peer_rating'] ), 1)],
            'selff_first':  [round ( float ( first_semester_avg  ['avgz_self_rating'] ), 1)],
            'spvs_second':  [round ( float ( second_semester_avg ['avgz_spvs_rating'] ), 1)],
            'stud_second':  [round ( float ( second_semester_avg ['avgz_stud_rating'] ), 1)],
            'peerr_second': [round ( float ( second_semester_avg ['avgz_peer_rating'] ), 1)],
            'selff_second': [round ( float ( second_semester_avg ['avgz_self_rating'] ), 1)],
            'spvs_second':  [round ( float ( summer_semester_avg ['avgz_spvs_rating'] ), 1)],
            'stud_second':  [round ( float ( summer_semester_avg ['avgz_stud_rating'] ), 1)],
            'peerr_second': [round ( float ( summer_semester_avg ['avgz_peer_rating'] ), 1)],
            'selff_second': [round ( float ( summer_semester_avg ['avgz_self_rating'] ), 1)],
        }

        first_semester_data = TableOne.objects.filter(semester='First', eval_year__year=present_date).order_by('semester', 'eval_year')
        first_semester_avg = first_semester_data.aggregate(
            avgz_spvs_rating=Avg('spvs_rating'),
            avgz_stud_rating=Avg('stud_rating'),
            avgz_peer_rating=Avg('peer_rating'),
            avgz_self_rating=Avg('self_rating') 
        )

        second_semester_data = TableOne.objects.filter(semester='Second', eval_year__year=present_date).order_by('semester', 'eval_year')
        second_semester_avg = second_semester_data.aggregate(
            avgz_spvs_rating=Avg('spvs_rating'),
            avgz_stud_rating=Avg('stud_rating'),
            avgz_peer_rating=Avg('peer_rating'),
            avgz_self_rating=Avg('self_rating')
        )

        summer_semester_data = TableOne.objects.filter(semester='Summer', eval_year__year=present_date).order_by('semester', 'eval_year')
        second_semester_avg = summer_semester_data.aggregate(
            avgz_spvs_rating=Avg('spvs_rating'),
            avgz_stud_rating=Avg('stud_rating'),
            avgz_peer_rating=Avg('peer_rating'),
            avgz_self_rating=Avg('self_rating')
        )
        overall_avg_first = (
            (float(first_semester_avg['avgz_spvs_rating'])) + 
            (float(first_semester_avg['avgz_stud_rating'])) + 
            (float(first_semester_avg['avgz_peer_rating'])) + 
            (float(first_semester_avg['avgz_self_rating']))
        ) / 4

        overall_avg_second = (
            (float(second_semester_avg['avgz_spvs_rating'])) + 
            (float(second_semester_avg['avgz_stud_rating'])) + 
            (float(second_semester_avg['avgz_peer_rating'])) + 
            (float(second_semester_avg['avgz_self_rating']))
        ) / 4

        overall_avg_summer = (
            (float(summer_semester_avg['avgz_spvs_rating'])) + 
            (float(summer_semester_avg['avgz_stud_rating'])) + 
            (float(summer_semester_avg['avgz_peer_rating'])) + 
            (float(summer_semester_avg['avgz_self_rating']))
        ) / 4

        overall_avg_first = round(overall_avg_first, 1)
        overall_avg_second = round(overall_avg_second, 1)
        overall_avg_summer = round(overall_avg_summer, 1)

        # count_one = TableOne.objects.filter(semester="First", eval_year__year=present_date).count()
        # count_two = TableOne.objects.filter(semester="Second", eval_year__year=present_date).count()

        overall_avg_first_percentage = (overall_avg_first / 5) * 100
        overall_avg_second_percentage = (overall_avg_second / 5) * 100
        overall_avg_summer_percentage = (overall_avg_summer / 5) * 100

        overall_avg_first_percentage = round(overall_avg_first_percentage, 0)
        overall_avg_second_percentage = round(overall_avg_second_percentage, 0)
        overall_avg_summer_percentage = round(overall_avg_summer_percentage, 0)
        
        overall_avg_dict = {
            'overall_avg_first': overall_avg_first_percentage,
            'overall_avg_second': overall_avg_second_percentage,
            'overall_avg_summer': overall_avg_summer_percentage,
        }

        # Serialize data dictionaries
        serialized_data_two = json.dumps(ave_per_catt)
        serialized_overall_avg = json.dumps(overall_avg_dict)

        if request.user.is_authenticated:
            first_name = request.user.first_name
            custom_data = User.objects.filter(first_name=first_name)  
        else:
            first_name = "" 
            #custom_data = []

        serialized_first_name = json.dumps(first_name)
        #serialized_custom_data = json.dumps(custom_data)

        # ==========     MASSIV RIS CONDITIONALS FOR DETAILED API ============= #

        token_url = os.environ.get('RIS_API_TOKEN')
        headers = {
            'Content-Type': 'application/json'
        }
        token_response = requests.get(token_url, headers=headers)

        if token_response.status_code == 200:
            data = token_response.json()
            token = data['result']['access_token']
            api_url = os.environ.get('RIS_API_URLZZ')
            
            headers = {
                'Authorization': f'Bearer {token}'
            }
            
            api_response = requests.get(api_url, headers=headers)
            
            if api_response.status_code == 200:
                ris_api_data = api_response.json()
                #return Response(ris_api_data)
            
                # # Research Publications Counted per Year
                # ris_api_data = os.environ.get('RIS_API_URLZZ')
                # response = requests.get(ris_api_data)
                # response.raise_for_status()
                # rsrch_data = response.json()

                totalresearch = len(ris_api_data)

                # Research Publications Percentaged per Year
                grouped_counted = {}
                total_count = 50
                for item in ris_api_data:
                    year = item['Publication Year'][:4]
                    grouped_counted.setdefault(year, {'count': 0})['count'] += 1

                percentage_data = {}
                for year, count in grouped_counted.items():
                    percentage_data[year] = {'percentage': (count['count'] / total_count * 100)}

                serialized_grouped_counted  = json.dumps(totalresearch)
                serialized_percentage_data  = json.dumps(percentage_data)

            else:
                return Response({'error': f"Failed to access API: {api_response.status_code} - {api_response.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': f"Failed to get token: {token_response.status_code} - {token_response.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # ==========     MASSIV RIS CONDITIONALS FOR DETAILED API ============= #

        context = {
            'total_research_papers' : serialized_grouped_counted ,
            'percent_research_papers' : serialized_percentage_data,
            'first_name'            : serialized_first_name      ,
            #'custom_data'           : serialized_custom_data    ,
            'chart_data_two'        : serialized_data_two        ,
            'overall_avg_data'      : serialized_overall_avg
        }
        return render(request, 'executive/exec_dashboard.html', context)
        
        # return JsonResponse(context, safe=False)