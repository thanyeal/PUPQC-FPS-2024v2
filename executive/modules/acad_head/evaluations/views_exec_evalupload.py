
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from executive.forms import ExcelUploadForm
from django.http import JsonResponse
from executive.models import TableOne
from django.contrib import messages
import pandas as pd

@login_required(login_url='login')
def evaluations(request):
    upload_successful = False
    data = []  # Data to be returned as JSON

    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            if excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file,  skiprows=1)
                for _, row in df.iterrows():
                    TableOne.objects.create(
                        faculty_num  = row['No.']             ,
                        facultyname  = row['Faculty Name']    ,
                        spvs_rating  = row['Rating']          ,
                        spvs_interp  = row['Interpretation']  ,
                        stud_rating  = row['Rating']          ,
                        stud_interp  = row['Interpretation']  ,
                        peer_rating  = row['Rating']          ,
                        peer_interp  = row['Interpretation']  ,
                        self_rating  = row['Rating']          ,
                        self_interp  = row['Interpretation']  ,
                        load_rating  = row['Rating']          ,
                        load_interp  = row['Interpretation']  ,
                        faculty_stat = row['Faculty Status']  ,
                        semester     = row['Semester']
                    )
                messages.success(request, 'File uploaded successfully')
                upload_successful = True
            else:
                messages.error(request, 'Wrong file type!')
                pass
    else:
        form = ExcelUploadForm()

    # Check if it's an AJAX request and return JSON data
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableOne.objects.all() 
        data = [{
                'faculty_num'   : item.faculty_num ,
                'facultyname'   : item.facultyname  ,
                'spvs_rating'   : item.spvs_rating  ,
                'spvs_interp'   : item.spvs_interp  ,
                'stud_rating'   : item.stud_rating  ,
                'stud_interp'   : item.stud_interp  ,
                'peer_rating'   : item.peer_rating  ,
                'peer_interp'   : item.peer_interp  ,
                'self_rating'   : item.self_rating  ,
                'self_interp'   : item.self_interp  ,
                'load_rating'   : item.load_rating  ,
                'load_interp'   : item.load_interp  ,
                'faculty_stat'  : item.faculty_stat ,
                'semester'      : item.semester
            } for item in queryset]
        return JsonResponse(data, safe=False)
    return render(request, 'executive/pages/eval_upload.html', {'form': form, 'upload_successful': upload_successful})
