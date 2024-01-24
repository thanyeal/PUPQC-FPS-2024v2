from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
import os, requests, json
from datetime import date

    # return render(request, 'executive/pages/rsrch_analytics.html')

@login_required(login_url='login')
def rsrch_analytics(request):
    target_year = date.today().year
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
            
                        
            try:
                
                ris_api_data = api_response.json()

                # Research Publications Per Category
                category_1 = [
                    item for item in ris_api_data
                    if  item.get('Category') == "CHED Recognized"
                ]
                category_2 = [
                    item for item in ris_api_data
                    if  item.get('Category') == "Web of Science"
                ]
                category_3 = [
                    item for item in ris_api_data
                    if  item.get('Category') == "Peer Reviewed"
                ]
                category_4 = [
                    item for item in ris_api_data
                    if  item.get('Category') == "Scopus"
                ]
                
                rsrch_category_1 = len( category_1 )
                rsrch_category_2 = len( category_2 )
                rsrch_category_3 = len( category_3 )
                rsrch_category_4 = len( category_4 )
                
                rsrch_categories = {
                    'CHED'  : rsrch_category_1,
                    'WEEB'  : rsrch_category_2,
                    'PEER'  : rsrch_category_3,
                    'SCOPUS': rsrch_category_4,
                }

                # Research Publications Grouped per Year
                grouped_data = {}
                for item in ris_api_data:
                    year = item['Publication Year'][:4]
                    grouped_data.setdefault(year, []).append(item)

                # # Research Publications Counted per Year
                grouped_counted = {}
                total_count = 50
                for item in ris_api_data:
                    year = item['Publication Year'][:4]
                    grouped_counted.setdefault(year, {'count': 0})['count'] += 1

                # Research Publications Percentaged per Year
                percentage_data = {}
                for year, count in grouped_counted.items():
                    percentage_data[year] = {'percentage': (count['count'] / total_count * 100)}

                # Research Publications Fetched Specific Year Today
                specific_year_data = percentage_data.get(str(target_year)) 


                grouped_counted_counts = {year: ris_api_data['count'] for year, ris_api_data in grouped_counted.items()}
                highest_year = int(max(grouped_counted_counts, key=grouped_counted_counts.get))
                lowest_year  = int(min(grouped_counted_counts, key=grouped_counted_counts.get))

                totalresearch = len(ris_api_data)

                slrzd_rsrch_categories   = json.dumps(   rsrch_categories  )
                slrzd_grouped_data       = json.dumps(   grouped_data      )
                slrzd_grouped_counted    = json.dumps(   grouped_counted   )
                slrzd_percentage_data    = json.dumps(   percentage_data   )
                slrzd_specific_year_data = json.dumps(  specific_year_data )
                slrzd_highest_year       = json.dumps(   highest_year      )
                slrzd_lowest_year        = json.dumps(   lowest_year       )
                slrzd_totalresearch      = json.dumps(   totalresearch     )
                
                context = {
                    'Categories'            : slrzd_rsrch_categories    ,
                    'Grouped Data'          : slrzd_grouped_data        ,
                    'js_grouped_counted'    : slrzd_grouped_counted     ,
                    'js_grouped_percent'    : slrzd_percentage_data       ,
                    'js_specific_data'      : slrzd_specific_year_data  ,
                    'js_highest_year'       : slrzd_highest_year        ,
                    'js_lowest_year'        : slrzd_lowest_year         ,
                    'js_totalresearch'      : slrzd_totalresearch
                }

                #return JsonResponse(context, safe=False)
                return render(request, 'executive/pages/rsrch_analytics.html', context)
            except requests.RequestException as e:
                return JsonResponse({'error': f'API request failed: {str(e)}'})
        else:
            return Response({'error': f"Failed to access API: {api_response.status_code} - {api_response.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': f"Failed to get token: {token_response.status_code} - {token_response.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



