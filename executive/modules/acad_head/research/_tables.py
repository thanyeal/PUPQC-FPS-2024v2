from executive.api import api_routes

def publications_table(request):
    ris_api_data = api_routes.get_ris_api(request)
    return ris_api_data