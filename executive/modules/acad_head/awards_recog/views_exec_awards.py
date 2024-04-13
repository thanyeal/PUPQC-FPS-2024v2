from django.shortcuts import render
from django.http import JsonResponse
# from executive.models import TableEight
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def awards_recog(request):
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     queryset = TableEight.objects.all() 
    #     data = [{
    #             'awards_faculty'    : item.awards_faculty   ,
    #             'awards_title'      : item.awards_title     ,
    #             'awards_date'       : item.awards_date      ,
    #             'awards_type'       : item.awards_type      ,
    #             'awards_status'     : item.awards_status 
    #         } for item in queryset]
    #     return JsonResponse(data, safe=False)
    return render(request, 'executive/pages/awards_recog.html')

