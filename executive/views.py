# from .modules.acad_head.feedbacks.views_exec_feedback_comms       import fac_contents
# from .modules.acad_head.feedbacks.views_exec_feedback_analytics   import fac_analytics
# from .modules.acad_head.retention_exits.views_exec_rt_anl         import retention_analytics
# from .modules.acad_head.retention_exits.views_exec_rt_ins         import retention_insights


from .modules.error_pages.views_error_404                         import error_page_404
from .modules.error_pages.views_error_500                         import error_page_500
from .modules.auth.views_registry                                 import registry
from .modules.auth.views_logout                                   import custom_logout
from .modules.acad_head.dashboard.views_exec_dashboard            import exec_dashboard
from .modules.acad_head.evaluations.views_exec_evalupload         import evaluations
from .modules.acad_head.evaluations.views_exec_evaluation         import eval_analytics
from .modules.acad_head.evaluations.views_exec_eval_list          import eval_list
from .modules.maintenance.views_comesoon                          import coming_soon
from .modules.acad_head.profile.views_exec_profilepage            import exec_p_page
from .modules.acad_head.profile.views_exec_profilesetting         import exec_p_sett
from .modules.acad_head.pro_dev.views_exec_prodev                 import prdv_wrkshp_att
from .modules.acad_head.pro_dev.views_exec_prodev_analytics       import prdv_wrkshp_anl
from .modules.acad_head.attend_leave.views_exec_alm_leaves        import alm_leaves_rec
from .modules.acad_head.attend_leave.views_exec_alm_analytics     import alm_analytics
from .modules.acad_head.awards_recog.views_exec_awards            import awards_recog
from .modules.acad_head.awards_recog.views_exec_awards_analytics  import awards_analytics
from .modules.acad_head.merit_prmot.views_exec_mrt_promotion      import mrt_promote
from .modules.acad_head.merit_prmot.views_exec_mrt_analytics      import mrt_analytics
from .modules.acad_head.research.views_exec_research              import rsrch_tracking
from .modules.acad_head.research.views_exec_research_analytics    import rsrch_analytics
from .modules.acad_head.workload.views_exec_workload              import workload_dat
from .modules.acad_head.workload.views_exec_workload_analytics    import workload_analytics
from .modules.acad_head.fac_mgmnt.views_faculty_management        import fac_mgmnt
from .modules.acad_head.fac_mgmnt.views_faculty_info              import faculty_info
from .modules.acad_head.fac_mgmnt.views_faculty_rep               import faculty_indiv_report
from .modules.acad_head.fac_mgmnt.views_faculty_reports           import faculty_mgmt_reports
from .modules.acad_head.fac_mgmnt.views_faculty_proc_data         import faculty_proc_data


# Authentication
registry
# log_in
custom_logout

# Errors
error_page_404
error_page_500

# Acad_Head
exec_dashboard

# Teaching Effectiveness
evaluations
eval_analytics
eval_list

# # Profile
exec_p_page
exec_p_sett

# # Research Publication
rsrch_analytics
rsrch_tracking

# # Professional Development    
prdv_wrkshp_att
prdv_wrkshp_anl

# # Attendance Leave Management
alm_analytics
alm_leaves_rec

# # Merit Promotions
mrt_analytics
mrt_promote

# # Workloads
workload_dat
workload_analytics

# # Awards and Recognition
awards_analytics
awards_recog

# Maintenance
coming_soon

#Faculty Management
fac_mgmnt
faculty_info
faculty_indiv_report
faculty_mgmt_reports
faculty_proc_data

# Retention Exit - Eliminated from the System
# retention_analytics
# retention_insights

# =====================================================================================================


from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from executive.config import route_config
import requests

@login_required(login_url='login')
@api_view(['GET'])
def testfacultyinfodata(request):
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
        return Response(fis_api_data)
    else:
        return Response({'error': f"Failed to access API: {fis_token_response.status_code} - {fis_token_response.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@login_required(login_url='login')
@api_view(['GET'])
def testresearchinfodata(request, format=None):
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
        return Response(ris_api_data)
    else:
        return Response({'error': f"Failed to access API: {ris_token_response.status_code} - {ris_token_response.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

