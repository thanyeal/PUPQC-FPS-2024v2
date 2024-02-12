from django.http import JsonResponse
from datetime import date
import os, requests, json, datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def fac_mgmnt(request):
    # API for Faculty Information System
    api_url = os.environ.get('FIS_API_EVALZ')
    response = requests.get(api_url)
    api_data = response.json()

    semesters = ['First', 'Second'] 
    faculty_name = None
                # specific_year = 2021  # Replace with the desired year
                # present_date = date(specific_year, 1, 1).year
                # present_date = date.today().year

    # API for Research Information System
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

    if request.method == 'POST':
        faculty_name_from_ajax = request.POST.get('faculty_name')
        faculty_name = faculty_name_from_ajax[:10].upper()
        faculty_name_in_logic = faculty_name

        ave_per_catt = {}
        for semester in semesters:
            semester_data = [
                entry for entry in api_data if entry.get('Semester') == semester and
                entry.get('FacultyName')[:10].upper() == faculty_name_in_logic #and
                # entry.get('Year', '').startswith(str(present_date))
            ]
            if semester_data:
                avg_spvs_rating = round(float(sum(float(entry['Supervisor Rating']) for entry in semester_data) / len(semester_data)), 1)
                avg_stud_rating = round(float(sum(float(entry['Students Rating'])   for entry in semester_data) / len(semester_data)), 1)
                avg_peer_rating = round(float(sum(float(entry['Peer Rating'])       for entry in semester_data) / len(semester_data)), 1)
                avg_self_rating = round(float(sum(float(entry['Self Rating'])       for entry in semester_data) / len(semester_data)), 1)
                ave_per_catt.update({
                    f'Supervisor_{semester}': [avg_spvs_rating],
                    f'Student_{semester}'   : [avg_stud_rating],
                    f'Peer_{semester}'      : [avg_peer_rating],
                    f'Self_{semester}'      : [avg_self_rating],
                })

        grouped_counted = {}
        for item in ris_api_data:
            if faculty_name in item.get('Author').upper():
                year = item.get('Publication Year')[:4]
                grouped_counted.setdefault(year, {'count': 0})['count'] += 1

        return JsonResponse({'faculty_mgmt': ave_per_catt, 'publication_counts': grouped_counted})
    return render(request, 'executive/pages/fac_mgmnt.html')