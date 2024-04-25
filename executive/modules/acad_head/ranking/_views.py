from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from executive.modules.acad_head.ranking._json  import performance_ranking, performance_headers
# import json
from django.http import JsonResponse
# from executive.api  import api_routes
# from executive.modules.acad_head.faculties._component_faculty   import individual_data
# from executive.modules.acad_head.research._tables               import publications_table
# from fuzzywuzzy import fuzz
# from collections import defaultdict


@login_required(login_url='login')
def pr_asView(request):
    try:
        researchers_performances = performance_ranking.research_ranking(request)
        evaluations_performances = performance_ranking.evaluations_ranking(request)
        context = {
            'research': researchers_performances,
            'evaluate': evaluations_performances
        }
        return JsonResponse(context, safe=False)
        # return render(request, 'executive/pages/performance_ranking.html', context)
    except KeyError as e:
        return {'error': str(e)}



# next task is identify per ranking per year, differentiate last year into current year
# add metrics in research
# missing entries in attendees, will not include professional development in ranking metrics
