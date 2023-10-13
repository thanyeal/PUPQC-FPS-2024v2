
# # from django.contrib.auth import login, authenticate
# # from executive.forms import CustomLoginForm
# # from django.contrib import messages
# # from django.shortcuts import render, redirect
    
# # def log_in(request):
# #     if request.method == "POST":
# #         form = CustomLoginForm(request, request.POST)
# #         if form.is_valid():
# #             username = form.cleaned_data['username']
# #             password = form.cleaned_data['password']
# #             user = authenticate(request, username=username, password=password)
# #             if user is not None:
# #                 login(request, user)
# #                 return redirect('exec_analytics')
# #             else:
# #                 messages.error(request, form.errors['__all__'])
# # # Inner Else tag not working +++
# #         else:
# #             error_message = form.errors['__all__'][0] if '__all__' in form.errors else 'Authentication failed.'
# #             messages.error(request, error_message)
# # # Inner Else tag not working +++
# #     else:
# #         form = CustomLoginForm()
# #     return render(request, 'registration/login.html', {'form': form, 'default_error_message': error_message})


# from django.contrib.auth import login, authenticate
# from executive.forms import CustomLoginForm
# from django.contrib import messages
# from django.shortcuts import render, redirect

# def log_in(request):
#     error_message = None  # Initialize error_message outside the if-else blocks

#     if request.method == "POST":
#         form = CustomLoginForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('exec_analytics')
#         else:
#             # Handle form errors
#             error_message = form.errors['__all__'][0] if '__all__' in form.errors else 'Authentication failed.'
#             messages.error(request, error_message)

#     else:
#         form = CustomLoginForm()

#     return render(request, 'registration/login.html', {'form': form, 'default_error_message': error_message})
