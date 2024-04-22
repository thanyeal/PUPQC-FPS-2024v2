from executive.api import api_routes
import json

def faculty_management_table(request):  
    fis_faculty_info = api_routes.get_fis_faculty_data(request)
    faculty_list = []
    for faculty_id, faculty_details in fis_faculty_info["Faculties"].items():
        faculty_name = f"{faculty_details['LastName']}, {faculty_details['FirstName']} {faculty_details['MiddleInitial']}."
        faculty_type = f"{faculty_details['FacultyType']}"
        faculty_rank = f"{faculty_details['Rank']}"
        faculty_addr = f"{faculty_details['ResidentialAddress']}"
        faculty_mail = f"{faculty_details['Email']}"
        faculty_numb = f"{faculty_details['MobileNumber']}"
        faculty_degr = f"{faculty_details['Degree']}"
        faculty_list.append({
            'Faculty_name': faculty_name,
            'Faculty_type': faculty_type,
            'Faculty_rank': faculty_rank,
            'Faculty_addr': faculty_addr,
            'Faculty_mail': faculty_mail,
            'Faculty_numb': faculty_numb,
            'Faculty_degr': faculty_degr
        })
    return faculty_list