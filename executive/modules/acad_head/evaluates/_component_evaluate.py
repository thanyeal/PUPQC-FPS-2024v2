from executive.api import api_routes

def evaluations(request):
    fis_te_api_data = api_routes.get_fis_te_api(request)
    result_list = []
    for data in fis_te_api_data:
        acad_head_avg = (data["acad_head_a"] + data["acad_head_b"] +
                        data["acad_head_c"] + data["acad_head_d"]) / 4.0
        self_avg = (data["self_a"] + data["self_b"] +
                    data["self_c"] + data["self_d"]) / 4.0
        director_avg = (data["director_a"] + data["director_b"] +
                    data["director_c"] + data["director_d"]) / 4.0
        student_avg = (data["student_a"] + data["student_b"] +
                    data["student_c"] + data["student_d"]) / 4.0
        result = {
            "Name": data["Name"],
            "Type": data["Type"],
            "school_year": data["school_year"],
            "semester": data["semester"],
            "acad_head_ave": round(acad_head_avg, 2),
            "self_ave": round(self_avg, 2),
            "director_ave": round(director_avg, 2),
            "student_ave": round(student_avg, 2),
        }
        result_list.append(result)

    return (result_list)