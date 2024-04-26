from executive.api import api_routes

def prodev_attendance(request):
    fis_prodev = api_routes.get_fis_prodev_data(request)
    fis_prodev_list = []
    
    for prodev_details in fis_prodev:
        program_title = prodev_details['title']
        program_start = prodev_details['date_start']
        program_end   = prodev_details['date_end']
        program_speaker = prodev_details['conducted_by']
        program_type = prodev_details['type']

        fis_prodev_list.append({
            'Program_Title'   : program_title,
            'Program_Start'   : program_start,
            'Program_End'     : program_end,
            'Program_Speaker' : program_speaker,
            'Program_Type'    : program_type
        })
    return (fis_prodev_list) 