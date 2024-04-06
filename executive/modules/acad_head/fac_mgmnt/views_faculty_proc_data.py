from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from executive.modules.acad_head.fac_mgmnt.views_faculty_rep import faculty_indiv_report
from collections import defaultdict
from datetime import datetime

@login_required(login_url='login')
def faculty_proc_data(request):
    fis_api_data = faculty_indiv_report(request)
    faculty_name = "Fernandez, Alma A."

    current_year = datetime.now().year
    academic_years_to_include = [f"{current_year - i}-{current_year - i + 1}" for i in range(4)]


    semesters_to_include = ["First", "Second"]
    faculty_data_dict = defaultdict(lambda: defaultdict(list))
    for item in fis_api_data:
        if (faculty_name in item.get('name')
                and item.get('school_year') in academic_years_to_include
                and item.get('semester') in semesters_to_include):

            school_year = item.get('school_year')
            student_calc_percentage = item.get('student_calc_percentage')
            acad_head_ave_percentage = item.get('acad_head_ave_percentage')
            semester = item.get('semester')

            faculty_data_dict[school_year][semester].append({
                'Student Percentage': student_calc_percentage,
                'Supervisor Percentage': acad_head_ave_percentage
            })

    result = []
    for academic_year, semesters in faculty_data_dict.items():
        for semester, percentages_list in semesters.items():
            total_student_percentage = sum(entry['Student Percentage'] for entry in percentages_list)
            total_supervisor_percentage = sum(entry['Supervisor Percentage'] for entry in percentages_list)
            num_entries = len(percentages_list)
            if num_entries != 0:
                average_student_percentage = total_student_percentage / num_entries
                average_supervisor_percentage = total_supervisor_percentage / num_entries
            else:
                average_student_percentage = 0
                average_supervisor_percentage = 0
            result.append({
                'Faculty Name': faculty_name,
                'Academic Year': "A.Y.  " + academic_year,
                'Average Student Percentage': average_student_percentage,
                'Average Supervisor Percentage': average_supervisor_percentage,
                'Semester': semester
            })

    return (result) #JsonResponse(result, safe=False)



