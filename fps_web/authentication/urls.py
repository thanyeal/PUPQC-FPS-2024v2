from .views import LoginView, RegistryView, LogoutView
from .validate_forms import EmailValidation, PasswValidation, LogEmailValidation, LogPasswValidation, LastnameValidation, FirstnameValidation, MiddlenameValidation
from django.urls import path
from django.views.decorators.csrf import csrf_exempt, csrf_protect

urlpatterns = [
    path('', csrf_protect(LoginView.as_view()), name="login"),
    path('', csrf_protect(LogoutView.as_view()), name="logout"),
    path('registry/', csrf_protect(RegistryView.as_view()), name="registry"),

    path('validate-email', csrf_exempt(EmailValidation.as_view()), name='validate_email'),
    path('validate-passw', csrf_exempt(PasswValidation.as_view()), name='validate_passw'),
    path('validate-webmail', csrf_exempt(LogEmailValidation.as_view()), name='validate_webmail'),
    path('validate-webpass', csrf_exempt(LogPasswValidation.as_view()), name='validate_webpass'),
    path('validate-lname', csrf_exempt(LastnameValidation.as_view()), name='validate_lname'),
    path('validate-fname', csrf_exempt(FirstnameValidation.as_view()), name='validate_fname'),
    path('validate-mname', csrf_exempt(MiddlenameValidation.as_view()), name='validate_mname'),

    
]