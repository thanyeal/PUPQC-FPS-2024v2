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
        
    @staticmethod
    def get_fis_te_api(request):
        fis_te_token = route_config.FIS_API_TE_TOKEN
        fis_te_token_key = fis_te_token
        fis_te_url = route_config.FIS_API_TE_URL
        fis_te_headers = {
            'Authorization': 'API Key',
            'token': fis_te_token_key,
            'Content-Type': 'application/json' 
        }
        fis_te_token_response = requests.get(fis_te_url, headers=fis_te_headers)
        if fis_te_token_response.status_code == 200:
            fis_te_api_data = fis_te_token_response.json()
            return fis_te_api_data
        else:
            return None
        
    @staticmethod
    def get_fis_faculty_data(request):
        fis_data_token = route_config.FIS_API_FACULTY_TOKEN
        fis_data_token_key = fis_data_token
        fis_data_url = route_config.FIS_API_FACULTY
        fis_data_headers = {
            'Authorization': 'API Key',
            'token': fis_data_token_key,
            'Content-Type': 'application/json' 
        }
        fis_data_token_response = requests.get(fis_data_url, headers=fis_data_headers)
        if fis_data_token_response.status_code == 200:
            fis_data_api_data = fis_data_token_response.json()
            return fis_data_api_data
        else:
            return None