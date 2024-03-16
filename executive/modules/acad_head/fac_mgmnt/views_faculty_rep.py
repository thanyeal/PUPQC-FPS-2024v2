from django.http import JsonResponse
from executive.api import api_routes
from django.contrib.auth.decorators import login_required
import requests

def convert_to_percentage(grade):
    max_grade = 5.0
    percentage = (grade / max_grade) * 100
    return '{:.4f}'.format(percentage)

def convert_to_interpretation(grade):
    # Legend for conversion
    legend = {
    (4.5, 5.0): 'Very Outstanding',
    (3.5, 4.49): 'Outstanding',
    (2.5, 3.49): 'Satisfactory',
    (1.5, 2.49): 'Fair',
    (1.0, 1.49): 'Poor'
    }

    for key, value in legend.items():
        if key[0] <= grade <= key[1]:
            return value


@login_required(login_url='login')
def faculty_indiv_report(request):  
    api_data1 = api_routes.get_fis_te_api(request)
    calculated_data_by_id = []

    for entry in api_data1:
        id = entry.get('id') 
        facultyid = entry.get('FacultyId')
        name = entry.get('Name')
        school_year = entry.get('school_year')
        type = entry.get('Type')
        semester = entry.get('semester')
        acad_head_a = entry.get('acad_head_a', 0)
        acad_head_b = entry.get('acad_head_b', 0)
        acad_head_c = entry.get('acad_head_c', 0)
        acad_head_d = entry.get('acad_head_d', 0)

        director_a = entry.get('director_a', 0)
        director_b = entry.get('director_b', 0)
        director_c = entry.get('director_c', 0)
        director_d = entry.get('director_d', 0)

        self_a = entry.get('self_a', 0)
        self_b = entry.get('self_b', 0)
        self_c = entry.get('self_c', 0)
        self_d = entry.get('self_d', 0)

        peer_a = entry.get('peer_a', 0)
        peer_b = entry.get('peer_b', 0)
        peer_c = entry.get('peer_c', 0)
        peer_d = entry.get('peer_d', 0)

        student_a = entry.get('student_a', 0)
        student_b = entry.get('student_b', 0)
        student_c = entry.get('student_c', 0)
        student_d = entry.get('student_d', 0)

        fac_evaluators = entry.get('fac_evaluators', 0)
        acad_head_evaluators = entry.get('acad_head_evaluators', 0)
        direktor_evaluators = entry.get('direktor_evaluators', 0)
        student_evaluators = entry.get('student_evaluators', 0)

        overall_evaluators = (
            acad_head_evaluators + fac_evaluators + direktor_evaluators + student_evaluators
        )
        
        # Calculate averages
        acad_head_ave = (acad_head_a + acad_head_b + acad_head_c + acad_head_d) / 4
        director_ave = (director_a + director_b + director_c + director_d) / 4
        self_ave = (self_a + self_b + self_c + self_d) / 4
        peer_ave = (peer_a + peer_b + peer_c + peer_d) / 4
        student_ave = (student_a + student_b + student_c + student_d) / 4

        # Calculate ratings BASED ON THE TEACHING EFFECTIVENES PERCENTAGES (STUDENT, PEER, SELF, DIRECTOR, ACAD HEAD)
        acad_head_calc = acad_head_ave * 0.10
        director_calc = director_ave * 0.20
        self_calc = self_ave * 1.0
        peer_calc = peer_ave * 0.20
        student_calc = student_ave * 0.70

        # AVERAGE RATE
        general_rating = acad_head_calc + director_calc + student_calc
        
        
        # CONVERSION TO PERCENTAGES
        self_ave_percentage         = round(float(convert_to_percentage(self_ave)), 2)
        student_ave_percentage      = round(float(convert_to_percentage(student_ave)), 2)
        peer_ave_percentage         = round(float(convert_to_percentage(peer_ave)), 2)
        director_ave_percentage     = round(float(convert_to_percentage(director_ave)), 2)
        acad_head_ave_percentage    = round(float(convert_to_percentage(acad_head_ave)), 2)
        
        # PERCENTAGES BASED ON TEACHING EFFECTIVENESS (STUDENT=70%,ACADHEAD=10%,DIRECTOR=20%,SELF=10%)
        self_calc_percentage        = float(convert_to_percentage(self_calc))
        student_calc_percentage     = float(convert_to_percentage(student_calc))
        director_calc_percentage    = float(convert_to_percentage(director_calc))
        acad_head_calc_percentage   = float(convert_to_percentage(acad_head_calc))
        

        
        calc_data = {
            # FACULTY INFO
            'facultyid': facultyid,
            'name': name,
            'school_year': school_year,
            'type': type,
            'semester': semester,
            
            # EVALUATION DATA
            'acad_head_a': acad_head_a,
            'acad_head_b': acad_head_b,
            'acad_head_c': acad_head_c,
            'acad_head_d': acad_head_d,
            'acad_head_ave': acad_head_ave,
            'acad_head_calc': acad_head_calc,
            'acad_head_interpret': convert_to_interpretation(acad_head_ave),
            
            'director_a': director_a,
            'director_b': director_b,
            'director_c': director_c,
            'director_d': director_d,
            'director_ave': director_ave,
            'director_calc': director_calc,
            'director_interpret': convert_to_interpretation(director_ave),
            
            'self_a': self_a,
            'self_b': self_b,
            'self_c': self_c,
            'self_d': self_d,
            'self_ave': self_ave,
            'self_calc': self_calc,
            'self_interpret': convert_to_interpretation(self_ave),
            
            'peer_a': peer_a,
            'peer_b': peer_b,
            'peer_c': peer_c,
            'peer_d': peer_d,
            'peer_ave': peer_ave,
            'peer_calc': peer_calc,
            'peer_interpret': convert_to_interpretation(peer_ave),
            
            'student_a': student_a,
            'student_b': student_b,
            'student_c': student_c,
            'student_d': student_d,
            'student_ave': student_ave,
            'student_calc': student_calc,
            'student_interpret': convert_to_interpretation(student_ave),
            
            'fac_evaluators': fac_evaluators,
            'acad_head_evaluators': acad_head_evaluators,
            'direktor_evaluators': direktor_evaluators,
            'student_evaluators': student_evaluators,
        
            'self_ave_percentage': self_ave_percentage,
            'student_ave_percentage': student_ave_percentage,
            'peer_ave_percentage': peer_ave_percentage,
            'director_ave_percentage': director_ave_percentage,
            'acad_head_ave_percentage': acad_head_ave_percentage,
            
            'self_calc_percentage': self_calc_percentage,
            'student_calc_percentage': student_calc_percentage,
            'director_calc_percentage': director_calc_percentage,
            'director_ave_percentage': director_ave_percentage,
            'acad_head_calc_percentage': acad_head_calc_percentage,
            
            # OVERALL
            'overall_average': self_calc_percentage + student_calc_percentage + director_calc_percentage + acad_head_calc_percentage, 
            'overall_evaluators': overall_evaluators,
            'general_rating': general_rating,
            'general_interpret': convert_to_interpretation(general_rating),
            
            
        }
        # calculated_data_by_id[id] = calc_data
        calculated_data_by_id.append(calc_data)
    
        
    # desired_id = 193 # SAMPLE ITEM ID FROM API DATA
    # desired_calc_data = calculated_data_by_id.get(desired_id, {})
    desired_calc_data = calculated_data_by_id
    #return JsonResponse(desired_calc_data, safe=False)
    return (desired_calc_data)