from django.http import HttpResponse
import io
import xlsxwriter
from collections import defaultdict
from datetime import datetime
from executive.modules.acad_head.faculties._component_faculty       import individual_data

def faculty_management_report(request):
    fis_api_data = individual_data(request)
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    faculty_name_from_ajax = request.POST.get('faculty_name')
    faculty_name = faculty_name_from_ajax
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
                average_student_percentage = round(total_student_percentage / num_entries, 2)
                average_supervisor_percentage = round(total_supervisor_percentage / num_entries, 2)
            else:
                average_student_percentage = 0
                average_supervisor_percentage = 0
            result.append({
                'Academic Year': academic_year,
                'Average Student Percentage': average_student_percentage,
                'Average Supervisor Percentage': average_supervisor_percentage,
                'Semester': semester
            }) # result = resultz
    # Cell Default Styles
    outlines = workbook.add_format({'border': 1})
    bold_outlines = workbook.add_format({'border': 2})
    # Row Formats
    row_a = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})
    row_b_col_a = workbook.add_format({'border': 1, 'color': 'gray'})
    row_b_col_b = workbook.add_format({'bold': True, 'border': 1})
    row_e = workbook.add_format({'border': 2, 'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': '#87CEEB'})
    row_f_col_a = workbook.add_format({'bold': True, 'align': 'right', 'valign': 'top'})
    row_f_col_b = workbook.add_format({'align': 'left', 'valign': 'top'})
    row_f_col_b.set_text_wrap()
    row_g_col_a = workbook.add_format({'bold': True, 'align': 'right', 'valign': 'top'})
    row_g_col_b = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'left'})
    row_h = workbook.add_format({'bold': True, 'valign': 'center'})
    row_h_col_b = workbook.add_format({'bold': True, 'valign': 'center', 'bg_color': '#93CC83'})
    row_i_col_a = workbook.add_format({'bold': True, 'valign': 'center'})
    row_i_col_b = workbook.add_format({'bold': True, 'valign': 'center', 'bg_color': '#93CC83'})
    row_i_col_c = workbook.add_format({'valign': 'center', 'bg_color': '#FFFCB3'})
    row_j_col_a = workbook.add_format({'align': 'center', 'valign': 'center'})
    row_j_col_b = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'center'})
    row_j_col_b_sub_a_d = workbook.add_format({'align': 'center','valign': 'center'})
    row_k = workbook.add_format({'align': 'center', 'valign': 'left'})
    row_k_datums = workbook.add_format({'valign': 'center', 'bg_color': '#FFFCB3'})
    row_l = workbook.add_format({'bold': True, 'valign': 'center', 'bg_color': '#DEDEDE'})
    # Headers (rows : seperated by new lines)
    worksheet.merge_range('B2:K3', 'KRA I - INSTRUCTION', row_a)
    # worksheet.write('B3', 'LAST NAME:' , row_b_col_a)
    # worksheet.merge_range('C3:K3', data['LAST NAME'] , row_b_col_b)
    # worksheet.write('B4', 'FIRST NAME, EXT.:' , row_b_col_a)
    # worksheet.merge_range('C4:K4', data['FIRST NAME, EXT.'] , row_b_col_b)
    # worksheet.write('B5', 'MIDDLE NAME:' , row_b_col_a)
    # worksheet.merge_range('C5:K5', data['MIDDLE NAME'] , row_b_col_b)
    worksheet.write('B5', 'FULLNAME' , row_b_col_a)
    worksheet.merge_range('C5:K5', faculty_name , row_b_col_b)
    worksheet.merge_range('B7:K7', 'CRITERION A - TEACHING EFFECTIVENESS (MAX = 60 POINTS)', row_e)
    worksheet.merge_range('B8:B11', '1.', row_f_col_a)
    worksheet.merge_range('C8:K11', 'FACULTY PERFORMANCE. Enter average rating received by the faculty/semester. For newly appointed faculty from private HEI, LUCs, TESDA/DepEd schools who still decided to proceed with the evaluation, put "0" in semesters with no student and supervisor\'s evaluation.', row_f_col_b)
    worksheet.write_rich_string('C8', workbook.add_format({'bold': True}), 'FACULTY PERFORMANCE.', workbook.add_format({'italic': True}), ' Enter average rating received by the faculty/semester. For newly appointed faculty from private HEI, LUCs, TESDA/DepEd schools who still decided to proceed with the evaluation, put "0" in semesters with no student and supervisor\'s evaluation.', row_f_col_b)
    worksheet.conditional_format('B8:K11', {'type': 'no_blanks', 'format': bold_outlines})
    # Student Eval Headers
    worksheet.write('B12', '1.1', row_g_col_a)
    worksheet.merge_range('C12:K12', 'STUDENT EVALUATION (60%)', row_g_col_b)
    worksheet.conditional_format('B12:K12', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('B13:J13', 'NUMBER OF SEMESTERS THAT WILL BE DEDUCTED FROM THE DIVISOR, IF APPLICABLE →', row_h)
    dlist_a = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    worksheet.write('K13', '0', row_h_col_b)
    worksheet.data_validation('K13', {'validate': 'list', 'source': dlist_a})
    worksheet.conditional_format('K13', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('B13:K13', {'type': 'no_blanks', 'format': bold_outlines})
    dlist_b = ['SELECT OPTION', 'NOT APPLICABLE', 'ON APPROVED STUDY LEAVE', 'ON APPROVED SABBATICAL LEAVE', 'ON APPROVED MATERNITY LEAVE']
    worksheet.merge_range('B14:G14', 'REASON FOR REDUCING THE DIVISOR', row_i_col_a)
    worksheet.merge_range('H14:I14', 'SELECT OPTION', row_i_col_b)
    worksheet.merge_range('J14:K14', '< link to Evidence from Google Drive >', row_i_col_c)
    worksheet.data_validation('H14:I14', {'validate': 'list', 'source': dlist_b})
    worksheet.conditional_format('B14:G14', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('H14:I14', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('J14:K14', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('B15:C16', 'Evaluation Period', row_j_col_a)
    worksheet.conditional_format('B15:C16', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('D15:K15', 'AVERAGE STUDENT EVALUATION RATING PER SEMESTER', row_j_col_b)
    worksheet.conditional_format('D15:K15', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('D16:E16', '1st SEMESTER', row_j_col_b_sub_a_d)
    worksheet.conditional_format('D16:E16', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('F16:G16', '< Evidence Link >', row_j_col_b_sub_a_d)
    worksheet.conditional_format('F16:G16', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('H16:I16', '2nd SEMESTER', row_j_col_b_sub_a_d)
    worksheet.conditional_format('H16:I16', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('J16:K16', '< Evidence Link >', row_j_col_b_sub_a_d)
    worksheet.conditional_format('J16:K16', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('B17:C17', 'a) AY 2020-2021', row_k)
    worksheet.merge_range('B18:C18', 'b) AY 2021-2022', row_k)
    worksheet.merge_range('B19:C19', 'c) AY 2022-2023', row_k)
    worksheet.merge_range('B20:C20', 'd) AY 2023-2024', row_k)
    worksheet.conditional_format('B17:C20', {'type': 'no_blanks', 'format': outlines})
    # First Sem Values
    for entry in result:
        academic_year = entry["Academic Year"]
        semester = entry["Semester"]
        student_percentage = entry["Average Student Percentage"]
        
        if semester == 'First':
            if academic_year == '2020-2021':
                worksheet.merge_range('D17:E17', student_percentage or '0', row_k_datums)
            elif academic_year == '2021-2022':
                worksheet.merge_range('D18:E18', student_percentage or '0', row_k_datums)
            elif academic_year == '2022-2023':
                worksheet.merge_range('D19:E19', student_percentage or '0', row_k_datums)
            elif academic_year == '2023-2024':
                worksheet.merge_range('D20:E20', student_percentage or '0', row_k_datums)
    worksheet.conditional_format('D17:E20', {'type': 'no_blanks', 'format': outlines})
    # First Sem Evidence Link
    worksheet.merge_range('F17:G17', '<>', row_k_datums)
    worksheet.merge_range('F18:G18', '<>', row_k_datums)
    worksheet.merge_range('F19:G19', '<>', row_k_datums)
    worksheet.merge_range('F20:G20', '<>', row_k_datums)
    worksheet.conditional_format('F17:G20', {'type': 'no_blanks', 'format': outlines})
    # Second Sem Values
    for entry in result:
        academic_year = entry["Academic Year"]
        semester = entry["Semester"]
        student_percentage = entry["Average Student Percentage"]
        
        if semester == 'Second':
            if academic_year == '2020-2021':
                worksheet.merge_range('H17:I17', student_percentage or '0', row_k_datums)
            elif academic_year == '2021-2022':
                worksheet.merge_range('H18:I18', student_percentage or '0', row_k_datums)
            elif academic_year == '2022-2023':
                worksheet.merge_range('H19:I19', student_percentage or '0', row_k_datums)
            elif academic_year == '2023-2024':
                worksheet.merge_range('H20:I20', student_percentage or '0', row_k_datums)
    worksheet.conditional_format('H17:I20', {'type': 'no_blanks', 'format': outlines})
    # Second Sem Evidence Link
    worksheet.merge_range('J17:K17', '<>', row_k_datums)
    worksheet.merge_range('J18:K18', '<>', row_k_datums)
    worksheet.merge_range('J19:K19', '<>', row_k_datums)
    worksheet.merge_range('J20:K20', '<>', row_k_datums)
    worksheet.conditional_format('J17:K20', {'type': 'no_blanks', 'format': outlines})
    # Student Rate: Overall Average Rating
    worksheet.merge_range('B21:I21', 'OVERALL AVERAGE RATING', row_l)
    student_rating_percentages = [entry['Average Student Percentage'] for entry in result]
    sr_overall_average = sum(student_rating_percentages) / len(student_rating_percentages)
    worksheet.merge_range('J21:K21', sr_overall_average or '0', row_l)
    # Student Rate: Faculty Score
    worksheet.merge_range('B22:I22', 'FACULTY SCORE', row_l)
    sr_score = sr_overall_average * 0.36
    sr_final_score = round(sr_score, 2)
    worksheet.merge_range('J22:K22', sr_final_score or '0', row_l)
    worksheet.conditional_format('B21:I21', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('J21:K21', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('B22:I22', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('J22:K22', {'type': 'no_blanks', 'format': bold_outlines})
    # Supervisor Eval Headers
    worksheet.write('B24', '1.2', row_g_col_a)
    worksheet.merge_range('C24:K24', "SUPERVISOR'S EVALUATION (40%)", row_g_col_b)
    worksheet.conditional_format('B24:K24', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('B25:J25', 'NUMBER OF SEMESTERS THAT WILL BE DEDUCTED FROM THE DIVISOR, IF APPLICABLE →', row_h)
    dlist_c = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    worksheet.write('K25', '0', row_h_col_b)
    worksheet.data_validation('K25', {'validate': 'list', 'source': dlist_c})
    worksheet.conditional_format('K25', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('B25:K25', {'type': 'no_blanks', 'format': bold_outlines})
    dlist_d = ['SELECT OPTION', 'NOT APPLICABLE', 'ON APPROVED STUDY LEAVE', 'ON APPROVED SABBATICAL LEAVE', 'ON APPROVED MATERNITY LEAVE']
    worksheet.merge_range('B26:G26', 'REASON FOR REDUCING THE DIVISOR', row_i_col_a)
    worksheet.merge_range('H26:I26', 'SELECT OPTION', row_i_col_b)
    worksheet.merge_range('J26:K26', '< link to Evidence from Google Drive >', row_i_col_c)
    worksheet.data_validation('H26:I26', {'validate': 'list', 'source': dlist_d})
    worksheet.conditional_format('B26:G26', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('H26:I26', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('J26:K26', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('B27:C28', 'Evaluation Period', row_j_col_a)
    worksheet.conditional_format('B27:C28', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('D27:K27', "SUPERVISOR'S RATING PER SEMESTER", row_j_col_b)
    worksheet.conditional_format('D27:K27', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('D28:E28', '1st SEMESTER', row_j_col_b_sub_a_d)
    worksheet.conditional_format('D28:E28', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('F28:G28', '< Evidence Link >', row_j_col_b_sub_a_d)
    worksheet.conditional_format('F28:G28', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('H28:I28', '2nd SEMESTER', row_j_col_b_sub_a_d)
    worksheet.conditional_format('H28:I28', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('J28:K28', '< Evidence Link >', row_j_col_b_sub_a_d)
    worksheet.conditional_format('J28:K28', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.merge_range('B29:C29', 'a) AY 2020-2021', row_k)
    worksheet.merge_range('B30:C30', 'b) AY 2021-2022', row_k)
    worksheet.merge_range('B31:C31', 'c) AY 2022-2023', row_k)
    worksheet.merge_range('B32:C32', 'd) AY 2023-2024', row_k)
    worksheet.conditional_format('B29:C32', {'type': 'no_blanks', 'format': outlines})
    # First Sem Values
    for entry in result:
        academic_year = entry["Academic Year"]
        semester = entry["Semester"]
        supervisor_percentage = entry["Average Supervisor Percentage"]
        
        if semester == 'First':
            if academic_year == '2020-2021':
                worksheet.merge_range('D29:E29', supervisor_percentage or '0', row_k_datums)
            elif academic_year == '2021-2022':
                worksheet.merge_range('D30:E30', supervisor_percentage or '0', row_k_datums)
            elif academic_year == '2022-2023':
                worksheet.merge_range('D31:E31', supervisor_percentage or '0', row_k_datums)
            elif academic_year == '2023-2024':
                worksheet.merge_range('D32:E32', supervisor_percentage or '0', row_k_datums)
    worksheet.conditional_format('D29:E32', {'type': 'no_blanks', 'format': outlines})
    # First Sem Evidence Link
    worksheet.merge_range('F29:G29', '<>', row_k_datums)
    worksheet.merge_range('F30:G30', '<>', row_k_datums)
    worksheet.merge_range('F31:G31', '<>', row_k_datums)
    worksheet.merge_range('F32:G32', '<>', row_k_datums)
    worksheet.conditional_format('F29:G32', {'type': 'no_blanks', 'format': outlines})
    # Second Sem Values
    for entry in result:
        academic_year = entry["Academic Year"]
        semester = entry["Semester"]
        supervisor_percentage = entry["Average Supervisor Percentage"]
        if semester == 'Second':
            if academic_year == '2020-2021':
                worksheet.merge_range('H29:I29', supervisor_percentage or '0', row_k_datums)
            elif academic_year == '2021-2022':
                worksheet.merge_range('H30:I30', supervisor_percentage or '0', row_k_datums)
            elif academic_year == '2022-2023':
                worksheet.merge_range('H31:I31', supervisor_percentage or '0', row_k_datums)
            elif academic_year == '2023-2024':
                worksheet.merge_range('H32:I32', supervisor_percentage or '0', row_k_datums)
    worksheet.conditional_format('H29:I32', {'type': 'no_blanks', 'format': outlines})
    # Second Sem Evidence Link
    worksheet.merge_range('J29:K29', '<>', row_k_datums)
    worksheet.merge_range('J30:K30', '<>', row_k_datums)
    worksheet.merge_range('J31:K31', '<>', row_k_datums)
    worksheet.merge_range('J32:K32', '<>', row_k_datums)
    worksheet.conditional_format('J29:K32', {'type': 'no_blanks', 'format': outlines})
    # Supervisor Rate: Overall Average Rating
    worksheet.merge_range('B33:I33', 'OVERALL AVERAGE RATING', row_l)
    supervisor_rating_percentages = [entry['Average Supervisor Percentage'] for entry in result]
    spr_overall_average = sum(supervisor_rating_percentages) / len(supervisor_rating_percentages)
    worksheet.merge_range('J33:K33', spr_overall_average or '0', row_l)
    # Supervisor Rate: Faculty Score
    worksheet.merge_range('B34:I34', 'FACULTY SCORE', row_l)
    spr_score = spr_overall_average * 0.36
    spr_final_score = round(spr_score, 2)
    worksheet.merge_range('J34:K34', spr_final_score or '0', row_l)
    worksheet.conditional_format('B33:I33', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('J33:K33', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('B34:I34', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.conditional_format('J34:K34', {'type': 'no_blanks', 'format': bold_outlines})
    worksheet.write('B36', 'Prepared by:',  workbook.add_format({'bold': True}))
    worksheet.merge_range('H36:I36', 'Evaluated by:',  workbook.add_format({'bold': True}))
    worksheet.merge_range('B39:C39', 'Name of Faculty and Signature')
    worksheet.write('B40', 'Date:')
    worksheet.merge_range('H39:I39', 'Name and Signature of IEC Member')
    worksheet.write('H40', 'Date:')
    worksheet.merge_range('H43:J43', 'Name and Signature of IEC Chair')
    worksheet.write('H44', 'Date:')

    try:
        workbook.close()
        faculty_name_for_filename = faculty_name.replace(',', '').replace('.', '').replace(' ', '_')
        filename = f"PUP-ISS_{faculty_name_for_filename}.xlsx"
        response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
    except Exception as e:
        return HttpResponse("Error generating report: {}".format(str(e)), status=500)