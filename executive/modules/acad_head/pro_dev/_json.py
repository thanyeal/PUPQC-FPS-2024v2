from executive.modules.acad_head.pro_dev._table import prodev_attendance
from datetime import datetime
from collections import Counter

class professional_development:
    def workshop_data(request):
        prodev_table = prodev_attendance(request)
        current_year = datetime.now().year
        past_two_years = [current_year - i for i in range(10)]
        program_counts = Counter()
        for entry in prodev_table:
            date_end = datetime.strptime(entry['Program_End'], '%a, %d %b %Y %H:%M:%S %Z')
            year = date_end.year
            if year in past_two_years:
                program_counts[year] += 1
        return (program_counts)

    def programtype_data(request):
        fis_prodev_list = prodev_attendance(request)
        type_counts = {}
        for program_details in fis_prodev_list:
            end_date = datetime.strptime(program_details['Program_End'], "%a, %d %b %Y %H:%M:%S %Z")
            year = end_date.year
            program_type = program_details['Program_Type'].lower() 
            if year not in type_counts:
                type_counts[year] = {}
            type_counts[year][program_type] = type_counts[year].get(program_type, 0) + 1
        return (type_counts)

    def progtypecount_data(request):
        fis_prodev_list = prodev_attendance(request)
        total_program_types = {} # not called
        total_count = 0
        for program in fis_prodev_list:
            program_type = program['Program_Type']
            total_program_types[program_type] = total_program_types.get(program_type, 0) + 1
            total_count += 1
        return (total_count)

    def prodevpresent_data(request):
        fis_prodev_list = prodev_attendance(request)
        present_year = datetime.now().year
        total_count_present_year = 0
        program_types_present_year = {} # not called
        for program in fis_prodev_list:
            program_year = datetime.strptime(program['Program_End'], "%a, %d %b %Y %H:%M:%S %Z").year
            if program_year == present_year:
                program_type = program['Program_Type']
                program_types_present_year[program_type] = program_types_present_year.get(program_type, 0) + 1
                total_count_present_year += 1
        return (total_count_present_year)

    def programcount_data(request):
        fis_prodev_list = prodev_attendance(request)
        types_counter = Counter(item['Program_Type'] for item in fis_prodev_list)
        type_counts = [{'type': type_, 'count': count} for type_, count in types_counter.items()]
        return (type_counts)

    def distinctprogram_data(request):
        fis_prodev_list = prodev_attendance(request)
        distinct_types = list(set(item['Program_Type'] for item in fis_prodev_list))
        return (distinct_types)