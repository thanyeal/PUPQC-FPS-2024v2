
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests, os

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
