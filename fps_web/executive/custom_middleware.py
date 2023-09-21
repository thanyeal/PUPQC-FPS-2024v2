# from django.shortcuts import redirect

# class RedirectToLoginMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Check if the current path is the root path '/'
#         if request.path == '/':
#             # Redirect to '/login' if the current path is '/'
#             return redirect('/login')
#         return self.get_response(request)
