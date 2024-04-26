from executive.api  import api_routes
from executive.modules.acad_head.faculties._component_faculty       import individual_data
from fuzzywuzzy import fuzz

class performance_ranking:
    @staticmethod
    def research_ranking(request):
        ris_data = api_routes.get_ris_api(request)
        fullname = api_routes.get_fis_faculty_data(request)
        result = []
        try:
            faculties = fullname["Faculties"]
            sorted_faculties = sorted(faculties.items(), key=lambda x: x[1]['LastName'])
            for faculty_id, faculty_details in sorted_faculties:
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
                        'Author': faculty_name,
                        'Ranking': research_pubs
                    })
            sorted_result = sorted(result, key=lambda x: x['Ranking'], reverse=True)
            ranked_result = []
            rank_counter = 1
            current_attends = sorted_result[0]['Ranking']
            for item in sorted_result:
                if item['Ranking'] < current_attends:
                    rank_counter += 1
                    current_attends = item['Ranking']
                item['Ranking'] = rank_counter
                ranked_result.append(item)
            return ranked_result
        except KeyError as e:
            raise KeyError(str(e))

    @staticmethod
    def evaluations_ranking(request):
        fis_eval = individual_data(request)
        fullname = api_routes.get_fis_faculty_data(request)
        result = []
        try:
            faculties = fullname["Faculties"]
            sorted_faculties = sorted(faculties.items(), key=lambda x: x[1]['LastName'])
            for faculty_id, faculty_details in sorted_faculties:
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
                        'Faculty': faculty_name,
                        'Ranking': round((4 / general_rate * 100), 2)
                    })
            sorted_result = sorted(result, key=lambda x: x['Ranking'], reverse=True)
            ranked_result = []
            rank_counter = 1
            current_attends = sorted_result[0]['Ranking']
            for item in sorted_result:
                if item['Ranking'] < current_attends:
                    rank_counter += 1
                    current_attends = item['Ranking']
                item['Ranking'] = rank_counter
                ranked_result.append(item)
            return ranked_result
        except KeyError as e:
            raise KeyError(str(e))

    @staticmethod
    def professional_dev(request):
        fullname_s = api_routes.get_fis_faculty_data(request)
        acmis_data = api_routes.get_acmis_data(request)['api_data']
        result = []
        try:
            faculties = fullname_s["Faculties"]
            sorted_faculties = sorted(faculties.items(), key=lambda x: x[1]['LastName'])
            for faculty_id, faculty_details in sorted_faculties:
                faculty_name = f"{faculty_details['LastName']}, {faculty_details['FirstName']} {faculty_details['MiddleInitial']}"
                matched = False
                attends_count = 0
                for item in acmis_data: 
                    attendee_name = item.get('FullName')
                    parts = attendee_name.split(',')
                    attendees = parts[0] + ',' + ''.join(parts[1:])
                    similarity_score = fuzz.ratio(attendee_name, faculty_name)
                    if similarity_score >= 80:
                        matched = True
                        attends_count += 1
                if matched:
                    result.append({
                        'Faculty': faculty_name,
                        'Ranking': attends_count
                    })
            sorted_result = sorted(result, key=lambda x: x['Ranking'], reverse=True)
            ranked_result = []
            rank_counter = 1
            current_attends = sorted_result[0]['Ranking']
            for item in sorted_result:
                if item['Ranking'] < current_attends:
                    rank_counter += 1
                    current_attends = item['Ranking']
                item['Ranking'] = rank_counter
                ranked_result.append(item)
            return ranked_result
        except KeyError as e:
            raise KeyError(str(e))