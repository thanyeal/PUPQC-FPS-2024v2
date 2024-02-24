
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests, os
from executive.config import route_config

@login_required(login_url='login')
def evaluations(request):
    data = []

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':

        fis_api_token =  route_config.FIS_API_TOKEN
        fis_token_key = fis_api_token
        fis_api_eval_url = route_config.FIS_API_EVALUATE_URL    
        fis_headers = {
            'Authorization': 'API Key'  ,
            'token': fis_token_key      ,
            'Content-Type': 'application/json' 
        }
        fis_token_response = requests.get(fis_api_eval_url, headers=fis_headers)

        if fis_token_response.status_code == 200:
            api_data = fis_token_response.json()
            data = api_data
        return JsonResponse(data, safe=False)
    return render(request, 'executive/pages/eval_upload.html')
