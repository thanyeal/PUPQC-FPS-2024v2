from executive.api import api_routes
from datetime import date
import json

def research_source(request):
    ris_api_source = api_routes.get_ris_api(request)
    return ris_api_source

def datetime_data(request):
    target_year = date.today().year
    return target_year

def publications_data(request):
    target_year = datetime_data(request)
    ris_api_source = research_source(request)
    if ris_api_source:
        think_response = 1

        # Research Publications Per Category
        category_1 = [
            item for item in ris_api_source
            if  item.get('Category') == "CHED Recognized"
        ]
        category_2 = [
            item for item in ris_api_source
            if  item.get('Category') == "Web of Science"
        ]
        category_3 = [
            item for item in ris_api_source
            if  item.get('Category') == "Peer Reviewed"
        ]
        category_4 = [
            item for item in ris_api_source
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
        for item in ris_api_source:
            year = item['Publication Year'][:4]
            grouped_data.setdefault(year, []).append(item)

        # # Research Publications Counted per Year
        grouped_counted = {}
        total_count = 50
        for item in ris_api_source:
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
        totalresearch = len(ris_api_source)

        serialized_response      = json.dumps(   think_response    )
        slrzd_rsrch_categories   = json.dumps(   rsrch_categories  )
        slrzd_grouped_data       = json.dumps(   grouped_data      )
        slrzd_grouped_counted    = json.dumps(   grouped_counted   )
        slrzd_percentage_data    = json.dumps(   percentage_data   )
        slrzd_specific_year_data = json.dumps(  specific_year_data )
        slrzd_highest_year       = json.dumps(   highest_year      )
        slrzd_lowest_year        = json.dumps(   lowest_year       )
        slrzd_totalresearch      = json.dumps(   totalresearch     )
    else:
        think_response = 0
        grouped_data = {"0": [{}]}
        rsrch_categories = {'': 0}
        grouped_counted = {'0': {'count': 0}}
        percentage_data = {'0': {'percentage': 0}}
        specific_year_data = 0
        highest_year = 0
        lowest_year = 0
        totalresearch = 0

        serialized_response      = json.dumps(   think_response    )
        slrzd_rsrch_categories   = json.dumps(   rsrch_categories  )
        slrzd_grouped_data       = json.dumps(   grouped_data      )
        slrzd_grouped_counted    = json.dumps(   grouped_counted   )
        slrzd_percentage_data    = json.dumps(   percentage_data   )
        slrzd_specific_year_data = json.dumps(  specific_year_data )
        slrzd_highest_year       = json.dumps(   highest_year      )
        slrzd_lowest_year        = json.dumps(   lowest_year       )
        slrzd_totalresearch      = json.dumps(   totalresearch     )

    
    
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'Categories'            : slrzd_rsrch_categories    ,
        'Grouped Data'          : slrzd_grouped_data        ,
        'js_grouped_counted'    : slrzd_grouped_counted     ,
        'js_grouped_percent'    : slrzd_percentage_data     ,
        'js_specific_data'      : slrzd_specific_year_data  ,
        'js_highest_year'       : slrzd_highest_year        ,
        'js_lowest_year'        : slrzd_lowest_year         ,
        'js_totalresearch'      : slrzd_totalresearch       ,
        'response_call'         : serialized_response       ,
        'requestz'              : serialized_state          ,
    }
    return context



# class publications_data:
    # def publication_categories(request):
    #     ris_api_source = research_source(request)
    #     category_1 = [
    #         item for item in ris_api_source
    #         if  item.get('Category') == "CHED Recognized"
    #     ]
    #     category_2 = [
    #         item for item in ris_api_source
    #         if  item.get('Category') == "Web of Science"
    #     ]
    #     category_3 = [
    #         item for item in ris_api_source
    #         if  item.get('Category') == "Peer Reviewed"
    #     ]
    #     category_4 = [
    #         item for item in ris_api_source
    #         if  item.get('Category') == "Scopus"
    #     ]
    #     rsrch_category_1 = len( category_1 )
    #     rsrch_category_2 = len( category_2 )
    #     rsrch_category_3 = len( category_3 )
    #     rsrch_category_4 = len( category_4 )
    #     rsrch_categories = {
    #         'CHED'  : rsrch_category_1,
    #         'WEEB'  : rsrch_category_2,
    #         'PEER'  : rsrch_category_3,
    #         'SCOPUS': rsrch_category_4,
    #     }
    #     return rsrch_categories

    # def grouped_publications(request):
    #     ris_api_source = research_source(request)
    #     grouped_data = {}
    #     for item in ris_api_source:
    #         year = item['Publication Year'][:4]
    #         grouped_data.setdefault(year, []).append(item)
    #     return grouped_data

    # def counted_group_data(request):
    #     ris_api_source = research_source(request)
    #     grouped_counted = {}
    #     for item in ris_api_source:
    #         year = item['Publication Year'][:4]
    #         grouped_counted.setdefault(year, {'count': 0})['count'] += 1
    #         return grouped_counted

    # def publication_percents(request):
    #     grouped_counted = publications_data.counted_group_data(request)
    #     total_count = 50
    #     percentage_data = {}
    #     for year, count in grouped_counted.items():
    #         percentage_data[year] = {'percentage': (count['count'] / total_count * 100)}
    #         return percentage_data

    # def specificyear_data(request):
    #     percentage_data = publications_data.publication_percents(request)
    #     target_year = datetime_data(request)
    #     specific_year_data = percentage_data.get(str(target_year)) 
    #     return specific_year_data

    # def highestpeak_data(request):
    #     ris_api_source = research_source(request)
    #     grouped_counted = publications_data.counted_group_data(request)
    #     grouped_counted_counts = {year: ris_api_source['count'] for year, ris_api_source in grouped_counted.items()}
    #     highest_year = int(max(grouped_counted_counts, key=grouped_counted_counts.get))
    #     return highest_year

    # def lowestpeak_data(request):
    #     ris_api_source = research_source(request)
    #     grouped_counted = publications_data.counted_group_data(request)
    #     grouped_counted_counts = {year: ris_api_source['count'] for year, ris_api_source in grouped_counted.items()}
    #     lowest_year  = int(min(grouped_counted_counts, key=grouped_counted_counts.get))
    #     return lowest_year

    # def totalpublications(request):
    #     ris_api_source = research_source(request)
    #     totalresearch = len(ris_api_source)
    #     return totalresearch