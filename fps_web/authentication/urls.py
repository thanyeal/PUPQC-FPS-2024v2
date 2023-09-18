from .views import LoginView, RegistryView, LogoutView
from .forms import EmailValidation, PasswValidation, LogEmail, LogPassw
from django.urls import path
from django.views.decorators.csrf import csrf_exempt, csrf_protect

urlpatterns = [
    # path('', csrf_exempt(LoginView.as_view()), name="login"),
    path('login/', csrf_exempt(LoginView.as_view()), name="login"),
    path('login/', csrf_exempt(LogoutView.as_view()), name="logout"),
    path('validate-email', csrf_exempt(EmailValidation.as_view()), name='validate_email'),
    path('validate-passw', csrf_exempt(PasswValidation.as_view()), name='validate_passw'),
    path('validate-webmail', csrf_exempt(LogEmail.as_view()), name='validate_webmail'),
    path('validate-webpass', csrf_exempt(LogPassw.as_view()), name='validate_webpass'),
    path('registry/', csrf_exempt(RegistryView.as_view()), name="registry"),
]