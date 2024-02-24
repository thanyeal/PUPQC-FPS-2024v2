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
from executive.api import api_routes

@login_required(login_url='login')
def rsrch_tracking(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        ris_api_data = api_routes.get_ris_api(request)
        return JsonResponse(ris_api_data, safe=False)
    return render(request, 'executive/pages/rsrch_tracking.html')
