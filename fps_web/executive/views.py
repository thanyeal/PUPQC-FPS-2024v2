import json
import pandas as pd

from decimal import Decimal

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models.functions import ExtractYear

from .models import TableOne
from .forms import ExcelUploadForm
from .forms import CustomRegistrationForm

from django.http import JsonResponse

# ! ++++++++++++++++++++++++++  for authentication views  ++++++++++++++++++++++++++++++ #

class RegistryView(View):
    def get(self, request):
        form = CustomRegistrationForm()
        return render(request, 'registration/registry.html', {'form': form})

    def post(self, request):
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Successfully registered!')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the form for errors.')
            return render(request, 'registration/registry.html', {'form': form})

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

def logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('login')

# ! ++++++++++++++++++++++++++  for main pages views  ++++++++++++++++++++++++++++++ #

@login_required(login_url='login')
def exec_dashboard(request):
    first_semester_data = TableOne.objects.filter(semester='First', eval_year__year=2023).order_by('semester', 'eval_year')
    first_semester_avg = first_semester_data.aggregate(
        avgz_spvs_rating=Avg('spvs_rating'),
        avgz_stud_rating=Avg('stud_rating'),
        avgz_peer_rating=Avg('peer_rating'),
        avgz_self_rating=Avg('self_rating') 
    )

    second_semester_data = TableOne.objects.filter(semester='Second', eval_year__year=2023).order_by('semester', 'eval_year')
    second_semester_avg = second_semester_data.aggregate(
        avgz_spvs_rating=Avg('spvs_rating'),
        avgz_stud_rating=Avg('stud_rating'),
        avgz_peer_rating=Avg('peer_rating'),
        avgz_self_rating=Avg('self_rating')
    )

    ave_per_catt = {
        'spvs_first':   [round ( float ( first_semester_avg  ['avgz_spvs_rating'] ), 2)],
        'stud_first':   [round ( float ( first_semester_avg  ['avgz_stud_rating'] ), 2)],
        'peerr_first':  [round ( float ( first_semester_avg  ['avgz_peer_rating'] ), 2)],
        'selff_first':  [round ( float ( first_semester_avg  ['avgz_self_rating'] ), 2)],
        'spvs_second':  [round ( float ( second_semester_avg ['avgz_spvs_rating'] ), 2)],
        'stud_second':  [round ( float ( second_semester_avg ['avgz_stud_rating'] ), 2)],
        'peerr_second': [round ( float ( second_semester_avg ['avgz_peer_rating'] ), 2)],
        'selff_second': [round ( float ( second_semester_avg ['avgz_self_rating'] ), 2)],
    }

    first_semester_data = TableOne.objects.filter(semester='First', eval_year__year=2023).order_by('semester', 'eval_year')
    first_semester_avg = first_semester_data.aggregate(
        avgz_spvs_rating=Avg('spvs_rating'),
        avgz_stud_rating=Avg('stud_rating'),
        avgz_peer_rating=Avg('peer_rating'),
        avgz_self_rating=Avg('self_rating') 
    )

    # Calculate the average for the second semester
    second_semester_data = TableOne.objects.filter(semester='Second', eval_year__year=2023).order_by('semester', 'eval_year')
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
    
    count_one = TableOne.objects.filter(semester="First", eval_year__year=2023).count()
    count_two = TableOne.objects.filter(semester="Second", eval_year__year=2023).count()

    overall_avg_first_percentage = (overall_avg_first / count_one) * 100
    overall_avg_second_percentage = (overall_avg_second / count_two) * 100

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
        custom_data = User.objects.filter(first_name=first_name)  # Replace with your query
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
    # return JsonResponse(context)

@login_required(login_url='login')
def evaluations(request):
    upload_successful = False
    data = []  # Data to be returned as JSON

    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            if excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file)
                for _, row in df.iterrows():
                    TableOne.objects.create(
                        facultyname=row['Faculty Name'],
                        spvs_rating=row['Supervisor Rating'],
                        spvs_interp=row['Supervisor Interpretation'],
                        stud_rating=row['Students Rating'],
                        stud_interp=row['Students Interpretation'],
                        peer_rating=row['Peer Rating'],
                        peer_interp=row['Peer Interpretation'],
                        self_rating=row['Self Rating'],
                        self_interp=row['Self Interpretation'],
                        semester=row['Semester']
                    )
                upload_successful = True
            else:
                # Handle unsupported file format
                pass
    else:
        form = ExcelUploadForm()

    # Check if it's an AJAX request and return JSON data
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableOne.objects.all() 
        data = [{
                'facultyname': item.facultyname,
                'spvs_rating': item.spvs_rating,
                'spvs_interp': item.spvs_interp,
                'stud_rating': item.stud_rating,
                'stud_interp': item.stud_interp,
                'peer_rating': item.peer_rating,
                'peer_interp': item.peer_interp,
                'self_rating': item.self_rating,
                'self_interp': item.self_interp,
                'semester': item.semester
            } for item in queryset]
        return JsonResponse(data, safe=False)

    return render(request, 'executive/pages/eval_upload.html', {'form': form, 'upload_successful': upload_successful})

# for in development page
@login_required(login_url='login')
def coming_soon(request):
    return render(request, 'coming_soon/coming_soon.html')

def convert_decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

@login_required(login_url='login')
def eval_analytics(request):
    # ==================================================================================================================================================================================
    chart_data = TableOne.objects.all()

    data = {
        'faculty': [item.facultyname for item in chart_data],
        'supervisor': [convert_decimal_to_float(item.spvs_rating) for item in chart_data],
        'student': [convert_decimal_to_float(item.stud_rating) for item in chart_data],
        'peer': [convert_decimal_to_float(item.peer_rating) for item in chart_data],
        'self': [convert_decimal_to_float(item.self_rating) for item in chart_data],
    }
    # ================================================================================================================================================================================== year

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

    # ================================================================================================================================================================================== data table
    # data table
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableOne.objects.all() 
        data = [{
                'facultyname': item.facultyname,
                'stud_rating': item.stud_rating,
                'stud_interp': item.stud_interp,
                'semester': item.semester,
            } for item in queryset]
        return JsonResponse(data, safe=False)
    # ================================================================================================================================================================================== teaching first data 
    first_semester_data = TableOne.objects.filter(semester='First', eval_year__year=2023).order_by('semester', 'eval_year')
    first_semester_avg = first_semester_data.aggregate(
        avgz_spvs_rating=Avg('spvs_rating'),
        avgz_stud_rating=Avg('stud_rating'),
        avgz_peer_rating=Avg('peer_rating'),
        avgz_self_rating=Avg('self_rating') 
    )

    second_semester_data = TableOne.objects.filter(semester='Second', eval_year__year=2023).order_by('semester', 'eval_year')
    second_semester_avg = second_semester_data.aggregate(
        avgz_spvs_rating=Avg('spvs_rating'),
        avgz_stud_rating=Avg('stud_rating'),
        avgz_peer_rating=Avg('peer_rating'),
        avgz_self_rating=Avg('self_rating')
    )

    ave_per_cattz = {
        'spvs_first':   [round ( float ( first_semester_avg  ['avgz_spvs_rating'] ), 2)],
        'stud_first':   [round ( float ( first_semester_avg  ['avgz_stud_rating'] ), 2)],
        'peerr_first':  [round ( float ( first_semester_avg  ['avgz_peer_rating'] ), 2)],
        'selff_first':  [round ( float ( first_semester_avg  ['avgz_self_rating'] ), 2)],
        'spvs_second':  [round ( float ( second_semester_avg ['avgz_spvs_rating'] ), 2)],
        'stud_second':  [round ( float ( second_semester_avg ['avgz_stud_rating'] ), 2)],
        'peerr_second': [round ( float ( second_semester_avg ['avgz_peer_rating'] ), 2)],
        'selff_second': [round ( float ( second_semester_avg ['avgz_self_rating'] ), 2)],
    }
    # ================================================================================================================================================================================== header

    first_semester_data = TableOne.objects.filter(semester='First', eval_year__year=2023).order_by('semester', 'eval_year')
    first_semester_avg = first_semester_data.aggregate(
        avgz_spvs_rating=Avg('spvs_rating'),
        avgz_stud_rating=Avg('stud_rating'),
        avgz_peer_rating=Avg('peer_rating'),
        avgz_self_rating=Avg('self_rating') 
    )

    # Calculate the average for the second semester
    second_semester_data = TableOne.objects.filter(semester='Second', eval_year__year=2023).order_by('semester', 'eval_year')
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
    
    count_one = TableOne.objects.filter(semester="First", eval_year__year=2023).count()
    count_two = TableOne.objects.filter(semester="Second", eval_year__year=2023).count()

    overall_avg_first_percentage = (overall_avg_first / count_one) * 100
    overall_avg_second_percentage = (overall_avg_second / count_two) * 100

    overall_avg_first_percentage = round(overall_avg_first_percentage, 0)
    overall_avg_second_percentage = round(overall_avg_second_percentage, 0)
    
    overall_avg_dict = {
        'overall_avg_first': overall_avg_first_percentage,
        'overall_avg_second': overall_avg_second_percentage
    }

    # ==================================================================================================================================================================================
    
    serialized_data_two = json.dumps(ave_per_cattz)
    serialized_data = json.dumps(data)
    serialized_overall_avg = json.dumps(overall_avg_dict)
    serialized_combined_data = json.dumps(combined_data)

    
    context = {
        'chart_data': serialized_data,
        'chart_data_two': serialized_data_two,
        'overall_avg_data': serialized_overall_avg,
        'combined_data': serialized_combined_data
    }

    return render(request, 'executive/pages/eval_analytics.html', context)
    # return JsonResponse(context, safe=False)