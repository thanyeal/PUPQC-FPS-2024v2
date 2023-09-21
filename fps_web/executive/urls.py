# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.exec_dashboard, name="exec_dashboard"),
#     path('evaluations', views.evaluations, name="evaluations")
# ]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import LoginView, RegistryView
# from .views import views
from .validate import EmailValidation, PasswValidation, LogEmailValidation, LogPasswValidation, LastnameValidation, FirstnameValidation, UsernameValidation
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # for main page
    path('', views.exec_dashboard, name="exec_dashboard"),
    path('dashboard', views.exec_dashboard, name="exec_dashboard"),
    path('evaluations', views.evaluations, name="evaluations"),

    # for maintenance page
    path('coming_soon', views.coming_soon,  name="coming_soon"),

    # for log and reg page
    path('', LoginView.as_view(), name="login"),
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
