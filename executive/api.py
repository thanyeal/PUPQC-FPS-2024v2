from django.contrib.auth.decorators import login_required
from executive.config import route_config
import requests
from django.http import JsonResponse


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
            # if not fis_api_data and fis_api_data["result"] is None:
            #     return None
            # else:
            return fis_api_data
        else:
            return None

        # try:
        #     fis_token_response = requests.get(fis_eval_url, headers=fis_headers)
        #     fis_token_response.raise_for_status()
        #     fis_api_data = fis_token_response.json()
                # if not fis_api_data and fis_api_data["result"] is None:
                #     return None
        # except requests.exceptions.RequestException as e:
        #     print(f"Error accessing RIS API: {e}")
        # except Exception as e:
        #     print(f"Unexpected error accessing RIS API: {e}")

    @staticmethod
    def get_ris_api(request):
        
        ris_rsrch_url = route_config.RIS_API_RESEARCH_URL
        ris_rsrch_alt = route_config.RIS_API_RESEARCH_ALT

        ris_token = route_config.RIS_API_TOKEN
        ris_alt_token = route_config.RIS_API_ALT_TOKEN

        ris_token_key = ris_token
        ris_alt_token_key = ris_alt_token
        
        ris_headers = {
            'Authorization': f'Bearer {ris_token_key}',
            'Content-Type'  : 'application/json' 
        }   
        
        ris_alt_headers = {
            'Authorization': 'API Key',
            'token': ris_alt_token_key,
            'Content-Type': 'application/json' 
        }
        try:
            ris_token_response = requests.get(ris_rsrch_url, headers=ris_headers)
            ris_token_response.raise_for_status()
            ris_api_data = ris_token_response.json()
            if ris_api_data['result'] is None:
                pass
            elif ris_api_data == []:
                pass
            else:
                return ris_api_data
        except requests.exceptions.RequestException as e:
            pass #return JsonResponse({"detail": f"Error accessing RIS API URL: {e}", "result": []})
        except Exception as e:
            pass #return JsonResponse({"detail": f"Unexpected error accessing RIS API URL: {e}", "result": []})

        try:
            ris_alt_token_response = requests.get(ris_rsrch_alt, headers=ris_alt_headers)
            ris_alt_token_response.raise_for_status()
            ris_api_alt_data = ris_alt_token_response.json()
            if ris_api_data or ris_api_data is not None:
                return ris_api_alt_data 
            elif ris_api_data is None or ris_api_alt_data == []:
                pass
        except requests.exceptions.RequestException as e:
            pass #return JsonResponse({"detail": f"Error accessing RIS API alternative URL: {e}", "result": []})
        except Exception as e:
            pass #return JsonResponse({"detail": f"Unexpected error accessing RIS API alternative URL: {e}", "result": []})

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
            # if not fis_te_api_data and fis_te_api_data["result"] is None:
            #     return None
            # else:
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
            # if not fis_data_api_data and fis_data_api_data["result"] is None:
            #     return None
            # else:
            return fis_data_api_data
        else:
            return None

    @staticmethod
    def get_fis_prodev_data(request):
        fis_prodev_data_token = route_config.FIS_API_PRODEV_TOKEN
        fis_prodev_key = fis_prodev_data_token
        fis_prodev_url = route_config.FIS_API_PRODEV

        fis_prodev_headers = {
            'Authorization': "API Key",
            'token': fis_prodev_key,
            'Content-Type': 'application/json'
        }

        fis_key_response = requests.get(fis_prodev_url, headers=fis_prodev_headers)
        if fis_key_response.status_code == 200:
            fis_data_prodev_api = fis_key_response.json()
            return fis_data_prodev_api
        else:
            return None