from executive.api  import api_routes
from executive.modules.acad_head.faculties._component_faculty       import individual_data
# from django.http import JsonResponse
from fuzzywuzzy import fuzz
from collections import defaultdict

def proffinfos_source(request):
    faculties = api_routes.get_fis_faculty_data(request)
    return faculties

def evaluation_source(request):
    fis_eval = api_routes.get_fis_eval_api(request)
    return fis_eval

def researches_source(request):
    ris_data = api_routes.get_ris_api(request)
    return ris_data

def developmnt_source(request):
    prd_data = api_routes.get_fis_prodev_data(request)
    return prd_data

class performance_ranking:
    @staticmethod
    def research_ranking(request):
        ris_data = api_routes.get_ris_api(request)
        fullname = api_routes.get_fis_faculty_data(request)
        result = []
        try:
            name_counts = defaultdict(int)
            for faculty_id, faculty_details in fullname["Faculties"].items():
                faculty_name = f"{faculty_details['LastName']}, {faculty_details['FirstName']} {faculty_details['MiddleInitial']}"
                matched = False
                research_pubs = 0
                for research in ris_data:
                    author = research.get('Author')
                    similarity_score = fuzz.ratio(faculty_name, author)
                    if similarity_score >= 80:
                        matched = True
                        research_pubs += 1
                        
                if matched: 
                    result.append({
                        'Faculty': faculty_name,
                        'status': matched,
                        'Research_Published': research_pubs
                    })
            sorted_result = sorted(result, key=lambda x: x['Research_Published'], reverse=True)
            return sorted_result
        except KeyError as e:
            raise KeyError(str(e))

    @staticmethod
    def evaluations_ranking(request):
        fis_eval = individual_data(request)
        fullname = api_routes.get_fis_faculty_data(request)
        result = []
        try:
            for faculty_id, faculty_details in fullname["Faculties"].items():
                faculty_name = f"{faculty_details['LastName']}, {faculty_details['FirstName']} {faculty_details['MiddleInitial']}"
                matched = False
                for faculty in fis_eval:
                    eval_name = faculty.get('name')
                    general_rate = faculty.get('overall_average')
                    similarity_score = fuzz.ratio(eval_name, faculty_name)
                    if similarity_score >= 80:
                        matched = True
                        break 
                if matched:
                    result.append({
                        'Faculty_name': faculty_name,
                        'Ranking': round((4 / general_rate * 100), 2)
                    })
            sorted_result = sorted(result, key=lambda x: x['Ranking'])
            return sorted_result
        except KeyError as e:
            raise KeyError(str(e))




    # def generalrate_data(request):
    #     pass

    # def gd_percentages(request):
    #     pass

    # def publication_data(request):
    #     pass

    # def pd_percentages(request):
    #     pass

    # def development_data(request):
    #     pass

    # def dd_percentages(request):
    #     pass

    # def top_performance(request):
    #     pass

    # def projects_ov_data(request):
    #     pass

class performance_headers:
    # def projects_no_data(request):
    #     pass

    # def projects_active(request):
    #     pass

    # def projects_revenue(request):
    #     pass

    def projects_hours(request):
        pass