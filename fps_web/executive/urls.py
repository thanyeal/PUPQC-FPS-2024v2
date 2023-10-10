from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import LoginView, RegistryView
from .validate import EmailValidation, PasswValidation, LogEmailValidation, LogPasswValidation, LastnameValidation, FirstnameValidation, UsernameValidation
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #for error pages
    path('error', views.error_page_404, name="error_page_404"),

    # for main page
    path('', views.exec_dashboard, name="exec_dashboard"),
    path('dashboard', views.exec_dashboard, name="exec_dashboard"),
    path('eval_upload', views.evaluations, name="eval_upload"),
    path('eval_analytics', views.eval_analytics, name="eval_analytics"),
    path('exec_profile', views.exec_p_page, name="exec_profile"),
    path('exec_settings', views.exec_p_sett, name="exec_settings"),

    # for maintenance page
    path('coming_soon', views.coming_soon,  name="coming_soon"),

    # for log and reg page
    path('login', LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registry/', RegistryView.as_view(), name="registry"),

    # for validation view for labels in the form
    path('validate-email', csrf_exempt(EmailValidation.as_view()), name=''),
    path('validate-passw', csrf_exempt(PasswValidation.as_view()), name=''),
    path('validate-webmail', csrf_exempt(LogEmailValidation.as_view()), name=''),
    path('validate-webpass', csrf_exempt(LogPasswValidation.as_view()), name=''),
    path('validate-lname', csrf_exempt(LastnameValidation.as_view()), name=''),
    path('validate-fname', csrf_exempt(FirstnameValidation.as_view()), name=''),
    path('validate-mname', csrf_exempt(UsernameValidation.as_view()), name=''),
]
