from executive.api  import api_routes

def ranking_table(request):
    acmis_data = api_routes.get_acmis_data(request)['api_data']
    ranking_table = []
    for ranking_details in acmis_data:
        fullname        = ranking_details['FullName']
        title           = ranking_details['title']
        activity_date   = ranking_details['date_end']
        types           = ranking_details['type']

        ranking_table.append({
            'name'  : fullname,
            'title' : title,
            'date'  : activity_date,
            'type'  : types
        })
    return ranking_table