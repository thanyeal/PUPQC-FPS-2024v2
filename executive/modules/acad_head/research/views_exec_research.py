# @login_required(login_url='login')
# def rsrch_tracking(request):
#     # Check if it's an AJAX request and return JSON data
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         queryset = TableFour.objects.all() 
#         data = [{
#                 'Author'            : item.rsrch_author         ,
#                 'Research Title'    : item.rsrch_title          ,
#                 'Publication Year'  : item.rsrch_year           ,
#                 'Publisher'         : item.rsrch_publisher      ,
#                 'Category'          : item.rsrch_category       ,
#                 'Author Type'       : item.rsrch_author_type    ,
#             } for item in queryset]
#         return JsonResponse(data, safe=False)
#     return render(request, 'executive/pages/rsrch_tracking.html')

from django.shortcuts import render
from django.http import JsonResponse
from executive.models import TableFour
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os, requests

@login_required(login_url='login')
def rsrch_tracking(request):
    api_url = os.environ.get('NEW_RIS_API_URL')

    # Check if it's an AJAX request and return JSON data
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response_one = requests.get(api_url)
        response_one.raise_for_status()
        data_one = response_one.json()
        return JsonResponse(data_one, safe=False)
    return render(request, 'executive/pages/rsrch_tracking.html')