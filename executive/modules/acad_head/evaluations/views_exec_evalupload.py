
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from executive.forms import ExcelUploadForm
from django.http import JsonResponse
from executive.models import TableOne
from django.contrib import messages
import pandas as pd
import requests, os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@login_required(login_url='login')
def evaluations(request):
    data = []  # Data to be returned as JSON

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Fetch data from the external API
        api_url = os.environ.get('FIS_API_EVALZ')
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()
            data = api_data
        return JsonResponse(data, safe=False)
    return render(request, 'executive/pages/eval_upload.html')
