from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ExcelUploadForm
from .models import TableOne
import json

from .forms import CustomRegistrationForm, CustomLoginForm
from django.conf import settings
import os
from django.http import FileResponse, JsonResponse
import pandas as pd


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
            return redirect('exec_dashboard')
        else:
            messages.error(request, 'Registration failed. Please check the form for errors.')
            return render(request, 'registration/registry.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = CustomRegistrationForm(data=request.POST)
        return render(request, 'registration/login.html', {'form': form})
    
    # def post(self, request):
    #     form = CustomLoginForm(data=request.POST)

    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')
    #         print(f"Email: {email}, Password: {password}")

    #         user = authenticate(email=email, password=password)
    #         print(user)

    #         if user is not None:
    #             login(request, user)
    #             messages.success(request, 'Successfully logged in!')
    #             return redirect('exec_dashboard')
    #         else:
    #             messages.error(request, 'Invalid credentials')
                
                
    #     else:
    #         messages.error(request, 'Invalid form submission')
    #     return render(request, 'registration/login.html', {'form': form})


# class LoginView(View):
#     def get(self, request):
#         form = CustomLoginForm()
#         return render(request, 'registration/login.html', {'form': form})

#     def post(self, request):
#         form = CustomLoginForm(data=request.POST)
#         if form.is_valid():
#             Email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             print(f"Email: {Email}, Password: {password}")

#             if Email and password is not None:
#                 check_password(password, password)
#                 user = User.objects.get(email=Email)
#                 authenticate(user)
#                 login(request, user)
#                 messages.success(request, 'Successfully logged in!')
#                 return redirect('exec_dashboard')
#             else:
#                 messages.error(request, 'Invalid credentials')
#                 print(user)
#         else:
#             messages.error(request, 'Invalid form submission')
#         return render(request, 'registration/login.html', {'form': form})

def logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('login')

# ! ++++++++++++++++++++++++++  for main pages views  ++++++++++++++++++++++++++++++ #

@login_required(login_url='login')
def exec_dashboard(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        custom_data = User.objects.filter(first_name='first_name')  # Replace with your query
    else:
        first_name = "" 
        custom_data = []
    return render(request, 'executive/exec_dashboard.html', {'first_name': first_name, 'custom_data': custom_data})

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
                    )
                upload_successful = True
            else:
                # Handle unsupported file format
                pass
    else:
        form = ExcelUploadForm()

    # Check if it's an AJAX request and return JSON data
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableOne.objects.all()  # Replace with your actual queryset
        print(queryset)
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
            } for item in queryset]
        return JsonResponse(data, safe=False)

    return render(request, 'executive/pages/evaluations.html', {'form': form, 'upload_successful': upload_successful})

# for in development page
@login_required(login_url='login')
def coming_soon(request):
    return render(request, 'coming_soon/coming_soon.html')

# // ++++++++++++++++++++++++++  for  something  views  ++++++++++++++++++++++++++++++ #


# @login_required(login_url='login')
# def test_eval_upload(request):
#     file_name = None

#     if request.method == 'POST':
#         uploaded_file = request.FILES['excel_file']

#         # Save the uploaded file to a temporary location
#         file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
#         with open(file_path, 'wb') as destination:
#             for chunk in uploaded_file.chunks():
#                 destination.write(chunk)

#         # Get the file name
#         file_name = uploaded_file.name

#         # Store the file name in session for displaying in another container
#         request.session['recently_uploaded_file'] = file_name

#         return redirect('test_evaluations')  # Redirect to the same page to display the file name

#     # Retrieve the most recent uploaded file name from the session
#     recently_uploaded_file = request.session.get('recently_uploaded_file')

#     # Define the directory where your Excel files are stored
#     excel_dir = settings.MEDIA_ROOT

#     # Get a list of all Excel files in the directory
#     excel_files = [f for f in os.listdir(excel_dir) if f.endswith('.xlsx')]

#     return render(request, 'executive/pages/test_evaluations.html', {'file_name': recently_uploaded_file, 'excel_files': excel_files})

# @login_required(login_url='login')
# def load_excel(request, file_name):
#     # Define the directory where your Excel files are stored
#     excel_dir = settings.MEDIA_ROOT
#     # Build the file path
#     file_path = os.path.join(excel_dir, file_name)
    
#     # Serve the file for download
#     excel_file = open(file_path, 'rb')
#     response = FileResponse(excel_file)
#     return response


# def view_excel(request, file_name):
#     # Define the directory where your Excel files are stored
#     excel_dir = settings.MEDIA_ROOT

#     # Build the file path
#     file_path = os.path.join(excel_dir, file_name)

#     # Read the Excel file into a DataFrame
#     try:
#         df = pd.read_excel(file_path)
#         # Assuming that the first row contains column headers
#         columns = df.columns.tolist()
#         data = df.values.tolist()
#     except Exception as e:
#         # Handle any errors when reading the Excel file
#         columns = []
#         data = []
    
#     return render(request, 'view_excel.html', {'columns': columns, 'data': data})

# @login_required(login_url='login')
# def test_eval_upload(request):
#     return render(request, 'executive/pages/test_evaluations.html')

# @login_required(login_url='login')
# def test_eval_upload(request):
#     upload_successful = False
#     data = []  # Data to be returned as JSON

#     if request.method == 'POST':
#         form = ExcelUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             excel_file = request.FILES['excel_file']
#             if excel_file.name.endswith('.xlsx'):
#                 df = pd.read_excel(excel_file)
#                 for _, row in df.iterrows():
#                     TableOne.objects.create(
#                         facultyname=row['Faculty Name'],
#                         spvs_rating=row['Supervisor Rating'],
#                         spvs_interp=row['Supervisor Interpretation'],
#                         stud_rating=row['Students Rating'],
#                         stud_interp=row['Students Interpretation'],
#                         peer_rating=row['Peer Rating'],
#                         peer_interp=row['Peer Interpretation'],
#                         self_rating=row['Self Rating'],
#                         self_interp=row['Self Interpretation'],
#                     )
#                 upload_successful = True
#             else:
#                 # Handle unsupported file format
#                 pass
#     else:
#         form = ExcelUploadForm()

#     # Check if it's an AJAX request and return JSON data
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         queryset = TableOne.objects.all()  # Replace with your actual queryset
#         print(queryset)
#         data = [{
#                 'facultyname': item.facultyname,
#                 'spvs_rating': item.spvs_rating,
#                 'spvs_interp': item.spvs_interp,
#                 'stud_rating': item.stud_rating,
#                 'stud_interp': item.stud_interp,
#                 'peer_rating': item.peer_rating,
#                 'peer_interp': item.peer_interp,
#                 'self_rating': item.self_rating,
#                 'self_interp': item.self_interp,
#             } for item in queryset]
#         return JsonResponse(data, safe=False)

#     return render(request, 'executive/pages/test_evaluations.html', {'form': form, 'upload_successful': upload_successful})