from django.contrib.auth.decorators import login_required
from django.db.models.functions import ExtractYear
from django.shortcuts import render, redirect
from executive.models import TableOne
from django.db.models import Avg
from decimal import Decimal
import json

@login_required(login_url='login')
def convert_decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

@login_required(login_url='login')
def eval_analytics(request):
    # ==================================================================================================================================================================================
    # chart_data = TableOne.objects.all()

    # data = {
    #     'faculty': [item.facultyname for item in chart_data],
    #     'supervisor': [convert_decimal_to_float(item.spvs_rating) for item in chart_data],
    #     'student': [convert_decimal_to_float(item.stud_rating) for item in chart_data],
    #     'peer': [convert_decimal_to_float(item.peer_rating) for item in chart_data],
    #     'self': [convert_decimal_to_float(item.self_rating) for item in chart_data],
    # }
    # ================================================================================================================================================================================== year
    if not TableOne.objects.exists():
        return redirect('error_page_404')
    else:
        first_semester_avg_by_year = (
            TableOne.objects.filter(semester='First')
            .annotate(eval_year_year=ExtractYear('eval_year'))
            .values('eval_year_year')
            .annotate(
                avg_spvs_rating=Avg('spvs_rating'),
                avg_stud_rating=Avg('stud_rating'),
                avg_peer_rating=Avg('peer_rating'),
                avg_self_rating=Avg('self_rating')
            )
        )

        # Group second semester data by year and calculate the average for each year
        second_semester_avg_by_year = (
            TableOne.objects.filter(semester='Second')
            .annotate(eval_year_year=ExtractYear('eval_year'))
            .values('eval_year_year')
            .annotate(
                avg_spvs_rating=Avg('spvs_rating'),
                avg_stud_rating=Avg('stud_rating'),
                avg_peer_rating=Avg('peer_rating'),
                avg_self_rating=Avg('self_rating')
            )
        )

        # Combine the data for both semesters by year
        combined_data = {}

        for entry in first_semester_avg_by_year:
            year = entry['eval_year_year']
            if year not in combined_data:
                combined_data[year] = {
                    'year': year,
                    'first_semester_avg': {},
                    'second_semester_avg': {},
                }
            combined_data[year]['first_semester_avg'] = {
                'avg_spvs_rating': entry['avg_spvs_rating'],
                'avg_stud_rating': entry['avg_stud_rating'],
                'avg_peer_rating': entry['avg_peer_rating'],
                'avg_self_rating': entry['avg_self_rating'],
            }

        for entry in second_semester_avg_by_year:
            year = entry['eval_year_year']
            if year not in combined_data:
                combined_data[year] = {
                    'year': year,
                    'first_semester_avg': {},
                    'second_semester_avg': {},
                }
            combined_data[year]['second_semester_avg'] = {
                'avg_spvs_rating': entry['avg_spvs_rating'],
                'avg_stud_rating': entry['avg_stud_rating'],
                'avg_peer_rating': entry['avg_peer_rating'],
                'avg_self_rating': entry['avg_self_rating'],
            }
        
        for year_data in combined_data.values():
            for semester_avg in [year_data['first_semester_avg'], year_data['second_semester_avg']]:
                for key, value in semester_avg.items():
                    semester_avg[key] = round(float(value) ,1)
        # ================================================================================================================================================================================== teaching first data 
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

        ave_per_cattz = {
            'spvs_first':   [round ( float ( first_semester_avg  ['avgz_spvs_rating'] ), 1)],
            'stud_first':   [round ( float ( first_semester_avg  ['avgz_stud_rating'] ), 1)],
            'peerr_first':  [round ( float ( first_semester_avg  ['avgz_peer_rating'] ), 1)],
            'selff_first':  [round ( float ( first_semester_avg  ['avgz_self_rating'] ), 1)],
            'spvs_second':  [round ( float ( second_semester_avg ['avgz_spvs_rating'] ), 1)],
            'stud_second':  [round ( float ( second_semester_avg ['avgz_stud_rating'] ), 1)],
            'peerr_second': [round ( float ( second_semester_avg ['avgz_peer_rating'] ), 1)],
            'selff_second': [round ( float ( second_semester_avg ['avgz_self_rating'] ), 1)],
        }
        # ================================================================================================================================================================================== header

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

        overall_avg_first = round(overall_avg_first, 3)
        overall_avg_second = round(overall_avg_second, 3)

        overall_avg_first_percentage = (overall_avg_first / 5) * 100
        overall_avg_second_percentage = (overall_avg_second / 5) * 100

        overall_avg_first_percentage = round(overall_avg_first_percentage, 0)
        overall_avg_second_percentage = round(overall_avg_second_percentage, 0)
        
        overall_avg_dict = {
            'overall_avg_first': overall_avg_first_percentage,
            'overall_avg_second': overall_avg_second_percentage
        }
        # ==================================================================================================================================================================================
        rating_above_3 = TableOne.objects.filter(stud_rating__gt=4.00)
        rating_below_3 = TableOne.objects.filter(stud_rating__lte=3.99)

        count_ra3 = rating_above_3.count()
        count_rb3 = rating_below_3.count()

        total_rec = TableOne.objects.all().count()

        pctg_ra3 = (count_ra3 / total_rec) * 100
        pctg_rb3 = (count_rb3 / total_rec) * 100

        pctg_ra3 = round(pctg_ra3, 2)
        pctg_rb3 = round(pctg_rb3, 2)

        two_ratings = {
            'pctg_ra3'  : pctg_ra3  ,
            'pctg_rb3'  : pctg_rb3  ,
            'count_ra3' : count_ra3 ,
            'count_rb3' : count_rb3
        }
        # ==================================================================================================================================================================================

        serialized_data_two      = json.dumps(ave_per_cattz)
        serialized_overall_avg   = json.dumps(overall_avg_dict)
        serialized_combined_data = json.dumps(combined_data)
        serialized_prctg_rating     = json.dumps(two_ratings)


        # serialized_data           = json.dumps(data)
        # serialized_combined_dataz = json.dumps(newbie)

        context = {
            # 'chart_data': serialized_data,
            # 'average_student': serialized_combined_dataz

            'chart_data_two'    : serialized_data_two       ,
            'overall_avg_data'  : serialized_overall_avg    ,
            'combined_data'     : serialized_combined_data  ,
            'percentage'  : serialized_prctg_rating 
        }
        return render(request, 'executive/pages/eval_analytics.html', context)

        #from django.http import JsonResponse
        #return JsonResponse(context, safe=False)
