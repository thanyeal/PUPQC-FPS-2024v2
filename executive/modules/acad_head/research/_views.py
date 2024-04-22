from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json
from executive.api import api_routes
from executive.modules.acad_head.research._tables import publications_table
from executive.modules.acad_head.research._json   import publications_data

@login_required(login_url='login')
def rs_asView(request):
    context = publications_data(request)
    return render(request, 'executive/pages/rsrch_analytics.html', context)


    # ris_api_data = api_routes.get_ris_api(request)
    # if ris_api_data:
    #     think_response = 1
    #     rsrch_categories    = publications_data.publication_categories(request)
    #     grouped_data        = publications_data.grouped_publications(request)
    #     grouped_counted     = publications_data.counted_group_data(request)
    #     percentage_data     = publications_data.publication_percents(request)
    #     specific_year_data  = publications_data.specificyear_data(request)
    #     highest_year        = publications_data.highestpeak_data(request)
    #     lowest_year         = publications_data.lowestpeak_data(request)
    #     totalresearch       = publications_data.totalpublications(request)
        
    #     serialized_response      = json.dumps(   think_response    )
    #     slrzd_rsrch_categories   = json.dumps(   rsrch_categories  )
    #     slrzd_grouped_data       = json.dumps(   grouped_data      )
    #     slrzd_grouped_counted    = json.dumps(   grouped_counted   )
    #     slrzd_percentage_data    = json.dumps(   percentage_data   )
    #     slrzd_specific_year_data = json.dumps(  specific_year_data )
    #     slrzd_highest_year       = json.dumps(   highest_year      )
    #     slrzd_lowest_year        = json.dumps(   lowest_year       )
    #     slrzd_totalresearch      = json.dumps(   totalresearch     )
    # else:
    #     think_response = 0
    #     grouped_data = {"0": [{}]}
    #     rsrch_categories = {'': 0}
    #     grouped_counted = {'0': {'count': 0}}
    #     percentage_data = {'0': {'percentage': 0}}
    #     specific_year_data = 0
    #     highest_year = 0
    #     lowest_year = 0
    #     totalresearch = 0

    #     serialized_response      = json.dumps(   think_response    )
    #     slrzd_rsrch_categories   = json.dumps(   rsrch_categories  )
    #     slrzd_grouped_data       = json.dumps(   grouped_data      )
    #     slrzd_grouped_counted    = json.dumps(   grouped_counted   )
    #     slrzd_percentage_data    = json.dumps(   percentage_data   )
    #     slrzd_specific_year_data = json.dumps(  specific_year_data )
    #     slrzd_highest_year       = json.dumps(   highest_year      )
    #     slrzd_lowest_year        = json.dumps(   lowest_year       )
    #     slrzd_totalresearch      = json.dumps(   totalresearch     )

    # state = 'active'
    # serialized_state = json.dumps(state)
    # context = {
    #     'Categories'            : slrzd_rsrch_categories    ,
    #     'Grouped Data'          : slrzd_grouped_data        ,
    #     'js_grouped_counted'    : slrzd_grouped_counted     ,
    #     'js_grouped_percent'    : slrzd_percentage_data     ,
    #     'js_specific_data'      : slrzd_specific_year_data  ,
    #     'js_highest_year'       : slrzd_highest_year        ,
    #     'js_lowest_year'        : slrzd_lowest_year         ,
    #     'js_totalresearch'      : slrzd_totalresearch       ,
    #     'response_call'         : serialized_response       ,
    #     'requestz'              : serialized_state          ,
    # }
    # #return JsonResponse(context, safe=False)
    # return render(request, 'executive/pages/rsrch_analytics.html', context)


@login_required(login_url='login')
def rt_asView(request):
    ris_api_data = publications_table(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(ris_api_data, safe=False)
    else:
        return JsonResponse(ris_api_data, safe=False)