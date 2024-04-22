from executive.api import api_routes
from executive.modules.acad_head.evaluates._component_evaluate     import evaluations
import json

def research_data(request):
    ris_api_data = api_routes.get_ris_api(request)
    return ris_api_data

def faculty_data(request):
    fis_evaluations = evaluations(request)
    return fis_evaluations

def evaluations_data(request):
    fis_evaluations = faculty_data(request)
    rating_above_3 = [item for item in fis_evaluations if float(item['student_ave']) > 4.00]
    rating_below_3 = [item for item in fis_evaluations if float(item['student_ave']) <= 3.99]
    count_ra3 = len(rating_above_3)
    count_rb3 = len(rating_below_3)
    total_rec = len(fis_evaluations)
    pctg_ra3 = (count_ra3 / total_rec) * 100
    pctg_rb3 = (count_rb3 / total_rec) * 100
    pctg_ra3 = round(pctg_ra3, 2)
    pctg_rb3 = round(pctg_rb3, 2)
    two_ratings = {
        'pctg_ra3': pctg_ra3    ,
        'pctg_rb3': pctg_rb3    ,
        'count_ra3': count_ra3  ,
        'count_rb3': count_rb3
    }
    highest_rated = count_ra3
    serialized_prctg_rating  = json.dumps(two_ratings)
    serialized_high_faculty  = json.dumps(highest_rated)
    return (serialized_prctg_rating, serialized_high_faculty)

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