# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.exec_dashboard, name="exec_dashboard"),
#     path('evaluations', views.evaluations, name="evaluations")
# ]

from django.urls import path
from . import views
from .views import LoginView, RegistryView, LogoutView
from .validate import EmailValidation, PasswValidation, LogEmailValidation, LogPasswValidation, LastnameValidation, FirstnameValidation, MiddlenameValidation
from django.views.decorators.csrf import csrf_protect, csrf_exempt

urlpatterns = [
    # for main page
    path('dashboard', views.exec_dashboard, name="exec_dashboard"),
    path('evaluations', views.evaluations, name="evaluations"),

    # for maintenance page
    path('coming_soon', views.coming_soon,  name="coming_soon"),

    # for log and reg page
    path('', csrf_protect(LoginView.as_view()), name="login"),
    path('', csrf_protect(LogoutView.as_view()), name="logout"),
    path('registry/', csrf_protect(RegistryView.as_view()), name="registry"),

    # for validation view for labels in the form
    path('validate-email', csrf_exempt(EmailValidation.as_view()), name='validate_email'),
    path('validate-passw', csrf_exempt(PasswValidation.as_view()), name='validate_passw'),
    path('validate-webmail', csrf_exempt(LogEmailValidation.as_view()), name='validate_webmail'),
    path('validate-webpass', csrf_exempt(LogPasswValidation.as_view()), name='validate_webpass'),
    path('validate-lname', csrf_exempt(LastnameValidation.as_view()), name='validate_lname'),
    path('validate-fname', csrf_exempt(FirstnameValidation.as_view()), name='validate_fname'),
    path('validate-mname', csrf_exempt(MiddlenameValidation.as_view()), name='validate_mname'),
]
