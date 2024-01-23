
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from executive.models import TableOne
from django.db.models import Avg
import json

@login_required(login_url='login')
def exec_dashboard(request):
    if not TableOne.objects.exists():
        return redirect('error_page_404')
    else:
        first_semester_data = TableOne.objects.filter(semester='First', eval_year__year=2024).order_by('semester', 'eval_year')
        first_semester_avg = first_semester_data.aggregate(
            avgz_spvs_rating=Avg('spvs_rating'),
            avgz_stud_rating=Avg('stud_rating'),
            avgz_peer_rating=Avg('peer_rating'),
            avgz_self_rating=Avg('self_rating') 
        )

        second_semester_data = TableOne.objects.filter(semester='Second', eval_year__year=2024).order_by('semester', 'eval_year')
        second_semester_avg = second_semester_data.aggregate(
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
        }

        first_semester_data = TableOne.objects.filter(semester='First', eval_year__year=2024).order_by('semester', 'eval_year')
        first_semester_avg = first_semester_data.aggregate(
            avgz_spvs_rating=Avg('spvs_rating'),
            avgz_stud_rating=Avg('stud_rating'),
            avgz_peer_rating=Avg('peer_rating'),
            avgz_self_rating=Avg('self_rating') 
        )

        # Calculate the average for the second semester
        second_semester_data = TableOne.objects.filter(semester='Second', eval_year__year=2024).order_by('semester', 'eval_year')
        second_semester_avg = second_semester_data.aggregate(
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

        overall_avg_first = round(overall_avg_first, 1)
        overall_avg_second = round(overall_avg_second, 1)

        # count_one = TableOne.objects.filter(semester="First", eval_year__year=2024).count()
        # count_two = TableOne.objects.filter(semester="Second", eval_year__year=2024).count()

        overall_avg_first_percentage = (overall_avg_first / 5) * 100
        overall_avg_second_percentage = (overall_avg_second / 5) * 100

        overall_avg_first_percentage = round(overall_avg_first_percentage, 0)
        overall_avg_second_percentage = round(overall_avg_second_percentage, 0)
        
        overall_avg_dict = {
            'overall_avg_first': overall_avg_first_percentage,
            'overall_avg_second': overall_avg_second_percentage
        }

        # Serialize data dictionaries
        serialized_data_two = json.dumps(ave_per_catt)
        serialized_overall_avg = json.dumps(overall_avg_dict)

        if request.user.is_authenticated:
            first_name = request.user.first_name
            custom_data = User.objects.filter(first_name=first_name)  
        else:
            first_name = "" 
            custom_data = []

        # Combine the contexts into a single dictionary
        context = {
            'first_name': first_name,
            'custom_data': custom_data,
            'chart_data_two': serialized_data_two,
            'overall_avg_data': serialized_overall_avg
        }
        return render(request, 'executive/exec_dashboard.html', context)
        
        # return JsonResponse(context, safe=False)