from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
class route_config:
    # Research Information System
    RIS_API_RESEARCH_URL    = "https://research-info-system-qegn.onrender.com/integration/faculty/research-papers/list"
    RIS_API_TOKEN           = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdF91c2VyIiwidG9rZW5fZ2VuZXJhdGUiOiJzdWNjZXNzIiwiY29ubmVjdGlvbl90eXBlIjoiZm9yIGludGVncmF0aW9uIn0.TYFxVaUUK-hbOMpWzcYhnXA4ZKQgeitWSrTyKpIuU-g"#"https://research-info-system-qegn.onrender.com/auth/integration/authentication"
    @classmethod
    def get_ris_api_url(cls):
        return cls.RIS_API_RESEARCH_URL
    @classmethod
    def get_ris_api_token(cls):
        return cls.RIS_API_TOKEN


    # Faculty Information System - Evaluations Module
    FIS_API_EVALUATE_URL    = "https://pupqcfis-com.onrender.com/api/FISFaculty/Evaluations"
    FIS_API_TOKEN           = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJjNmYzMDFjZTg3OWE0M2YwOWMyZWYyZjUzODk1YjY1OSJ9.L0Xs2-s2hAhnOuUEyciVLPHOHDtH3OAeC_UgoMP3X64"
    @classmethod
    def get_fis_api_eval_url(cls):
        return cls.FIS_API_EVALUATE_URL
    @classmethod
    def get_fis_api_token(cls):
        return cls.FIS_API_TOKEN


    # Faculty Information System - Faculty Records



    # Extension Services Information System