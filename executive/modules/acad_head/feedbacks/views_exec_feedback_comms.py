from django.shortcuts import render
from django.http import JsonResponse
from executive.models import TableSeven

def fac_contents(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        queryset = TableSeven.objects.all() 
        data = [{
                "eval_faculty" : item.eval_faculty,
                "eval_type"    : item.eval_type,
                "eval_person"  : item.eval_person,
                "eval_score"   : item.eval_score,
                "eval_comms"   : item.eval_comms,
            } for item in queryset]
        return JsonResponse(data, safe=False)   
    return render(request, 'executive/pages/fac_contents.html')