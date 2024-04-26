from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from executive.modules.acad_head.ranking._json   import performance_ranking
from executive.api  import api_routes
from django.http import JsonResponse
from django.http import HttpResponseServerError
import json

# from executive.api  import api_routes
# from executive.modules.acad_head.faculties._component_faculty   import individual_data
# from executive.modules.acad_head.research._tables               import publications_table
# from fuzzywuzzy import fuzz
# from collections import defaultdict
# import json

@login_required(login_url='login')
def pr_asView(request):

    # context = api_routes.get_acmis_data(request)
    # context = {
    #     'x': fromz
    # }
    # return JsonResponse(context, safe=False)

    try:
        researchers_performances = performance_ranking.research_ranking(request)
        evaluations_performances = performance_ranking.evaluations_ranking(request)
        professions_performances = performance_ranking.professional_dev(request)
        state = 'active'
        serialized_state = json.dumps(state)
        context = {
            'research': researchers_performances,
            'evaluate': evaluations_performances,
            'profesnl': professions_performances
        }
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(context, safe=False)
        else:
            return render(request, 'executive/pages/performance_ranking.html', {'requestz': serialized_state})
            # return JsonResponse(context, safe=False)
    except KeyError as e:
        error_message = str(e)
        return HttpResponseServerError("An error occurred: {}".format(error_message))

# next task is identify per ranking per year, differentiate last year into current year
# add metrics in research
# missing entries in attendees, will not include professional development in ranking metrics
