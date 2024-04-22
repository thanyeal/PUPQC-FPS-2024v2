from executive.api import api_routes
from executive.modules.acad_head.faculties._component_faculty       import individual_data
from executive.modules.acad_head.faculties._table                   import faculty_management_table
from executive.modules.acad_head.evaluates._component_evaluate     import evaluations

class faculty_managemet_module:
    def research_data(request):
        ris_api_data = api_routes.get_ris_api(request)
        return ris_api_data

    def faculty_data(request):
        fis_overalls = evaluations(request)
        return fis_overalls

    def faculties_table(request):
        fis_table = faculty_management_table(request)
        return fis_table

class faculty_management:

    def categories_data(request):
        fis_api_data = individual_data(request)
        semesters = ['First', 'Second'] 
        faculty_name = None 
        faculty_name_from_ajax = request.POST.get('faculty_name')
        faculty_name = faculty_name_from_ajax[:10].upper()
        faculty_name_in_logic = faculty_name 
        average_categories = {}
        for semester in semesters:
            semester_data = [
                entry for entry in fis_api_data if entry.get('semester') == semester and
                entry.get('name')[:10].upper() == faculty_name_in_logic #and
                # entry.get('Year', '').startswith(str(present_date))
            ]
            if semester_data:
                avg_spvs_rating = round(sum(float(entry['acad_head_calc_percentage']) for entry in semester_data) / len(semester_data), 1)
                avg_stud_rating = round(sum(float(entry['student_calc_percentage'  ]) for entry in semester_data) / len(semester_data), 1)
                avg_dirc_rating = round(sum(float(entry['director_calc_percentage' ]) for entry in semester_data) / len(semester_data), 1)
                avg_self_rating = round(sum(float(entry['self_calc_percentage'     ]) for entry in semester_data) / len(semester_data), 1)
                average_categories.update({
                    f'Supervisor_{semester}': [avg_spvs_rating],
                    f'Student_{semester}'   : [avg_stud_rating],
                    f'Director_{semester}'  : [avg_dirc_rating],
                    f'Self_{semester}'      : [avg_self_rating],
                })
        return average_categories

    def publication_data(request):
        ris_api_data = faculty_managemet_module.research_data(request)
        faculty_name = None 
        faculty_name_from_ajax = request.POST.get('faculty_name')
        faculty_name = faculty_name_from_ajax[:10].upper() 
        research_counted = {}
        for item in ris_api_data:
            if faculty_name in item.get('Author').upper():
                year = item.get('Publication Year')[:4]
                research_counted.setdefault(year, {'count': 0})['count'] += 1
        return research_counted

    def overallrate_data(request):
        fis_overalls = faculty_managemet_module.faculty_data(request)
        faculty_name = None 
        semesters = ['First', 'Second'] 
        faculty_name_from_ajax = request.POST.get('faculty_name')
        faculty_name = faculty_name_from_ajax[:10].upper() 
        overall_ratings = {}
        for faculty in fis_overalls:
            if faculty_name in faculty.get('Name')[:10].upper():
                academic_year = str(faculty['school_year'][:9])
                overall_ratings.setdefault(academic_year, {})
                for sem in semesters:
                    overall_ratings[academic_year][sem.lower() + '_sem_rating'] = {
                        'acadhead_rating' : faculty['acad_head_ave'],
                        'individs_rating' : faculty['self_ave'],
                        'director_rating' : faculty['director_ave'], 
                        'students_rating' : faculty['student_ave'],
                    }
        return overall_ratings

    def facultyinfo_data(request):
        fis_informat = faculty_managemet_module.faculties_table(request)
        faculty_name = None 
        faculty_name_from_ajax = request.POST.get('faculty_name')
        faculty_name = faculty_name_from_ajax[:10].upper() 
        indiv_information = {}
        for individual in fis_informat:
            if faculty_name == individual.get('Faculty_name')[:10].upper():
                indiv_information = {
                    'faculty_name': individual.get('Faculty_name'),
                    'faculty_type': individual.get('Faculty_type'),
                    'faculty_rank': individual.get('Faculty_rank'),
                    'faculty_addr': individual.get('Faculty_addr'),
                    'faculty_mail': individual.get('Faculty_mail'),
                    'faculty_numb': individual.get('Faculty_numb'),
                    'faculty_degr': individual.get('Faculty_degr'),
                }
        return indiv_information

    def progressbar_data(request):
        fis_api_data =  individual_data(request)
        faculty_name = None 
        faculty_name_from_ajax = request.POST.get('faculty_name')
        faculty_name = faculty_name_from_ajax[:10].upper() 
        faculty_progress = {}
        for progresses in fis_api_data:
            if faculty_name in progresses.get('name')[:10].upper():
                general_rating = progresses.get('general_rating')
                rounded_rating = round(general_rating, 2)
                partial_percentage = min(rounded_rating / 5 * 100, 100)
                final_percentage = round(partial_percentage, 2)
                faculty_progress.update({
                    'overall_percent': final_percentage
                })
        return faculty_progress
