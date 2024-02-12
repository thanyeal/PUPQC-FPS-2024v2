# from django.http import JsonResponse
# from django.shortcuts import render
# import json
# # from django.views.decorators.csrf import csrf_exempt

# # @csrf_exempt
# def testing_num1(request):

#     # Check if it's an AJAX request
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         faculty_name = request.POST.get('faculty_name')
#         response_data = {'message': '{}'.format(faculty_name)}
#         return JsonResponse(response_data)
from django.http import JsonResponse

def testing_num1(request):
    if request.method == 'POST':
        faculty_name = request.POST.get('faculty_name')
        # Process the faculty_name as needed
        return JsonResponse({'faculty_name': faculty_name})
    else:
        faculty_name = request.COOKIES.get('faculty_name')  # Attempt to retrieve from session
        if faculty_name:
            return JsonResponse({'faculty_name': faculty_name})
        else:
            return JsonResponse({'error': 'Faculty name not found'})
