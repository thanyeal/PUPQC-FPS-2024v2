from executive.api import api_routes
from decimal import Decimal
from executive.modules.acad_head.evaluates._component_evaluate     import evaluations
import json, datetime

def convert_decimal_to_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj

def teacheffectiveness_data(request):
    _evaluations = evaluations(request)
    return _evaluations

class evaluations_module:
    def evaluations_data(request):
        json_response = teacheffectiveness_data(request)
        grouped_data = {}   
        for item in json_response:
            eval_year = item['school_year']
            year = eval_year[:4]
            semester = item['semester']
            if year not in grouped_data:
                grouped_data[year] = {
                    'First': {
                        'avgz_spvs_rating': [],
                        'avgz_stud_rating': [],
                        'avgz_peer_rating': [],
                        'avgz_self_rating': []
                    },
                    'Second': {
                        'avgz_spvs_rating': [],
                        'avgz_stud_rating': [],
                        'avgz_peer_rating': [],
                        'avgz_self_rating': []
                    },
                    'Summer': {
                        'avgz_spvs_rating': [],
                        'avgz_stud_rating': [],
                        'avgz_peer_rating': [],
                        'avgz_self_rating': []
                    }
                }
            grouped_data[year][semester]['avgz_spvs_rating'].append(item['acad_head_ave'])
            grouped_data[year][semester]['avgz_stud_rating'].append(item['student_ave'])
            grouped_data[year][semester]['avgz_peer_rating'].append(item['director_ave'])
            grouped_data[year][semester]['avgz_self_rating'].append(item['self_ave'])
        for year, year_data in grouped_data.items():
            for semester, semester_data in year_data.items():
                for rating_type, ratings in semester_data.items():
                    if len(ratings) > 0:
                        semester_data[rating_type] = round(sum(float(rating) for rating in ratings) / len(ratings), 1)
                    else:
                        semester_data[rating_type] = 0.0
        ave_per_cattz = [
            {
                'year': year,
                'frst_semester_avg': year_data['First'],
                'scnd_semester_avg': year_data['Second'],
                'summer_semester_avg': year_data['Summer']
            }
            for year, year_data in grouped_data.items()
        ]
        ave_per_cattz.sort(key=lambda x: x['year'])        
        current_year = datetime.datetime.now().year
        terminal_year = current_year - 1
        current_year_data = grouped_data[str(terminal_year)]

        overall_avg_dict = {}
        for semester, semester_data in current_year_data.items():
            if semester in ['First', 'Second']: 
                overall_avg_for_semester = (
                    float(semester_data['avgz_spvs_rating']) +
                    float(semester_data['avgz_stud_rating']) +
                    float(semester_data['avgz_peer_rating']) +
                    float(semester_data['avgz_self_rating'])
                ) / 4
                overall_avg_for_semester = round(overall_avg_for_semester, 3)
                overall_avg_percentage = (overall_avg_for_semester / 5) * 100
                overall_avg_percentage = round(overall_avg_percentage, 0)
                key_name = f"overall_avg_{semester.lower()}"
                overall_avg_dict[key_name] = overall_avg_percentage
        serialized_data_two      = json.dumps(ave_per_cattz)
        serialized_overall_avg   = json.dumps(overall_avg_dict)

        return serialized_data_two, serialized_overall_avg

    def countandrating_data(request):
        json_response = teacheffectiveness_data(request)
        rating_above_3 = [item for item in json_response if float(item['student_ave']) > 4.00]
        rating_below_3 = [item for item in json_response if float(item['student_ave']) <= 3.99]
        count_ra3 = len(rating_above_3)
        count_rb3 = len(rating_below_3)
        total_rec = len(json_response)
        pctg_ra3 = (count_ra3 / total_rec) * 100
        pctg_rb3 = (count_rb3 / total_rec) * 100
        pctg_ra3 = round(pctg_ra3, 2)
        pctg_rb3 = round(pctg_rb3, 2)
        two_ratings = {
            'pctg_ra3'  : pctg_ra3    ,
            'pctg_rb3'  : pctg_rb3    ,
            'count_ra3' : count_ra3   ,
            'count_rb3' : count_rb3
        }
        serialized_prctg_rating  = json.dumps(two_ratings)

        return serialized_prctg_rating

