# # from django.shortcuts import redirect

# # class RedirectToLoginMiddleware:
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         # Check if the current path is the root path '/'
# #         if request.path == '/':
# #             # Redirect to '/login' if the current path is '/'
# #             return redirect('/login')
# #         return self.get_response(request)

from django.contrib.auth.decorators import login_required
from executive.config import route_config
import requests


@login_required(login_url='login')
class api_routes:

    @staticmethod
    def get_fis_eval_api(request):
        selected_token = route_config.FIS_API_TOKEN
        fis_token_key = selected_token
        fis_eval_url = route_config.FIS_API_EVALUATE_URL
        fis_headers = {
            'Authorization': 'API Key',
            'token': fis_token_key,
            'Content-Type': 'application/json' 
        }
        fis_token_response = requests.get(fis_eval_url, headers=fis_headers)
        
        if fis_token_response.status_code == 200:
            fis_api_data = fis_token_response.json()
            return fis_api_data
        else:
            return None

    @staticmethod
    def get_ris_api(request):
        ris_token = route_config.RIS_API_TOKEN
        ris_token_key = ris_token
        ris_rsrch_url = route_config.RIS_API_RESEARCH_URL
        ris_headers = {
            'Authorization': f'Bearer {ris_token_key}',
            'Content-Type'  : 'application/json' 
        }   
        ris_token_response = requests.get(ris_rsrch_url, headers=ris_headers)
        
        if ris_token_response.status_code == 200:
            ris_api_data = ris_token_response.json()
            return ris_api_data
        else:
            return None