from executive.api import api_routes
from executive.modules.acad_head.evaluates._component_evaluate     import evaluations
from datetime import date
import json
from executive.modules.acad_head.faculties._table                   import faculty_management_table

def faculties_table(request):
    fis_table = faculty_management_table(request)
    return fis_table

def research_source(request):
    ris_api_source = api_routes.get_ris_api(request)
    return ris_api_source

def datetime_data(request):
    target_year = date.today().year
    return target_year

def research_data(request):
    ris_api_data = api_routes.get_ris_api(request)
    return ris_api_data

def faculty_data(request):
    fis_evaluations = evaluations(request)
    return fis_evaluations

def evaluations_data(request):
    fis_informat = faculties_table(request)
    count_rb3 = len(fis_informat)
    serialized_high_faculty  = json.dumps(count_rb3)
    return (serialized_high_faculty) 

    # fis_evaluations = faculty_data(request)
    # rating_above_3 = [item for item in fis_evaluations if float(item['student_ave']) > 4.00]
    # rating_below_3 = [item for item in fis_evaluations if float(item['student_ave']) <= 3.99]
    # count_ra3 = len(rating_above_3)
    # count_rb3 = len(rating_below_3)
    # total_rec = len(fis_evaluations)
    # pctg_ra3 = (count_ra3 / total_rec) * 100
    # pctg_rb3 = (count_rb3 / total_rec) * 100
    # pctg_ra3 = round(pctg_ra3, 2)
    # pctg_rb3 = round(pctg_rb3, 2)
    # two_ratings = {
    #     'pctg_ra3': pctg_ra3    ,
    #     'pctg_rb3': pctg_rb3    ,
    #     'count_ra3': count_ra3  ,
    #     'count_rb3': count_rb3
    # }
    # highest_rated = count_ra3
    # serialized_prctg_rating  = json.dumps(two_ratings)
    # serialized_high_faculty  = json.dumps(highest_rated)
    # return (serialized_prctg_rating, serialized_high_faculty)

def publications_data(request):
    ris_api_data = research_data(request)
    if ris_api_data:
        think_response = 1
        totalresearch = len(ris_api_data)
        grouped_counted = {}
        total_count = 50
        for item in ris_api_data:
            if 'Publication Year' in item and item['Publication Year'] and isinstance(item['Publication Year'], str):
                year = int(item['Publication Year'][:4])
                grouped_counted.setdefault(year, {'count': 0})['count'] += 1
        percentage_data = {}
        for year, count in grouped_counted.items():
            percentage_data[year] = {'percentage': (count['count'] / total_count * 100)}
        serialized_grouped_counted = json.dumps(totalresearch)
        serialized_percentage_data = json.dumps(percentage_data)
        serialized_response = json.dumps(think_response)
    else:
        think_response = 0
        totalresearch = 0
        percentage_data = {'percentage': 0}
        serialized_grouped_counted = json.dumps(totalresearch)
        serialized_percentage_data = json.dumps(percentage_data)
        serialized_response = json.dumps(think_response)
    return (serialized_grouped_counted, serialized_percentage_data, serialized_response)

def authentications(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
    else:   
        first_name = ""
    serialized_first_name = json.dumps(first_name)
    return serialized_first_name

def rpublicatiob_data(request):
    target_year = datetime_data(request)
    ris_api_source = research_source(request)
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
    slrzd_rsrch_categories   = json.dumps(   rsrch_categories  )
    slrzd_grouped_data       = json.dumps(   grouped_data      )
    slrzd_grouped_counted    = json.dumps(   grouped_counted   )
    slrzd_percentage_data    = json.dumps(   percentage_data   )
    slrzd_specific_year_data = json.dumps(  specific_year_data )
    slrzd_highest_year       = json.dumps(   highest_year      )
    slrzd_lowest_year        = json.dumps(   lowest_year       )
    slrzd_totalresearch      = json.dumps(   totalresearch     )
    return  slrzd_grouped_counted