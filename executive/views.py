# from .modules.acad_head.feedbacks.views_exec_feedback_comms       import fac_contents
# from .modules.acad_head.feedbacks.views_exec_feedback_analytics   import fac_analytics
# from .modules.acad_head.retention_exits.views_exec_rt_anl         import retention_analytics
# from .modules.acad_head.retention_exits.views_exec_rt_ins         import retention_insights


from .modules.error_pages.views_error_404                         import error_page_404
from .modules.auth.views_registry                                 import registry
from .modules.auth.views_logout                                   import custom_logout
from .modules.acad_head.dashboard.views_exec_dashboard            import exec_dashboard
from .modules.acad_head.evaluations.views_exec_evalupload         import evaluations
from .modules.acad_head.evaluations.views_exec_evaluation         import eval_analytics
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

# Authentication
registry
# log_in
custom_logout

# Errors
error_page_404

# Acad_Head
exec_dashboard
evaluations
eval_analytics

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

# Retention Exit - Eliminated from the System
# retention_analytics
# retention_insights

# Faculty - Eliminated from the System
# fac_analytics
# fac_contents

# =====================================================================================================

from django.http import JsonResponse
from executive.models import TableTwo
from .serializers import TableTwoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests, os


@api_view(['GET'])
def testapifrompostmanshit(request, format=None):
    # try:
        response = requests.get('https://covid-api.com/api/regions')
        response.raise_for_status()
        data = response.json()
        return Response(data)
    # except requests.exceptions.RequestException as e:
        # return Response({'error': str(e)}, status=500)  # Handle errors gracefully



@api_view(['GET'])
def testresearchinfodata(request, format=None):
    token_url = os.environ.get('RIS_API_TOKEN')
    headers = {
        'Content-Type': 'application/json'
    }
    token_response = requests.get(token_url, headers=headers)
    
    if token_response.status_code == 200:
        data = token_response.json()
        token = data['result']['access_token']
        api_url = os.environ.get('RIS_API_URLZZ')
        
        headers = {
            'Authorization': f'Bearer {token}'
        }
        
        api_response = requests.get(api_url, headers=headers)
        
        if api_response.status_code == 200:
            ris_api_data = api_response.json()
            return Response(ris_api_data)
        else:
            return Response({'error': f"Failed to access API: {api_response.status_code} - {api_response.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': f"Failed to get token: {token_response.status_code} - {token_response.text}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['GET'])
def testfacultyinfodata(request, format=None):
    response_two = requests.get('https://pupqcfis-com.onrender.com/api/all/FISFaculty')
    response_two.raise_for_status()
    data_two = response_two.json()
    return Response(data_two)

@api_view(['GET', 'POST'])
def table_list(request, format=None):
    if request.method == 'GET':
        table2 = TableTwo.objects.all()
        serializer = TableTwoSerializer(table2, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False) # Also, it can set a list into dictionary by using this format {'var': var2.data, safe=False}
    
    if request.method == 'POST':
        serializer = TableTwoSerializer(data=request.data)
        if serializer.is_valid():           
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def table2_detail(request, id, format=None):
    try:
        tablez = TableTwo.objects.get(pk=id)
    except TableTwo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TableTwoSerializer(tablez)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TableTwoSerializer(tablez, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tablez.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)