from django.urls import path
from . import views
from executive.views import CustomLoginView
from .validate import EmailValidation, PasswValidation, LogEmailValidation, LogPasswValidation, LastnameValidation, FirstnameValidation, UsernameValidation
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path("",          views.db_asView , name="dashboard"), 
    path("dashboard", views.db_asView , name="dashboard"),

    path("faculties", views.fm_asView , name="faculties"), 
    path("facultyfn", views.fn_asView , name="facultyfn"), 
    path("facultyfo", views.fo_asView , name="facultyfo"), 
    path("facultyfp", views.fp_asView , name="facultyfp"), 

    path("evales_el", views.el_asView , name="evales_el"), 
    path("evales_em", views.em_asView , name="evales_em"), 

    path("publicate", views.rs_asView , name="publicate"), 
    path("public_tb", views.rt_asView , name="public_tb"), 

    path("prodev_a" , views.pd_asView , name="prodev_a" ),
    path("prodev_b" , views.pe_asView , name="prodev_b" ),

    path("rankings" , views.pr_asView , name="rankings" ),

    path('error_404'        , views.error_page_404  , name="error_page_404" ),
    path('error_500'        , views.error_page_500  , name="error_page_500" ),
    
    path('exec_profile'     , views.exec_p_page     , name="exec_profile"   ),
    path('exec_settings'    , views.exec_p_sett     , name="exec_settings"  ),

    path('coming_soon'      , views.coming_soon     , name="coming_soon"),

    path('registry/'        , views.registry        , name="registry"   ),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),

    path('validate-email'   , csrf_exempt(EmailValidation.as_view())    , name=''),
    path('validate-passw'   , csrf_exempt(PasswValidation.as_view())    , name=''),
    path('validate-webmail' , csrf_exempt(LogEmailValidation.as_view()) , name=''),
    path('validate-webpass' , csrf_exempt(LogPasswValidation.as_view()) , name=''),
    path('validate-lname'   , csrf_exempt(LastnameValidation.as_view()) , name=''),
    path('validate-fname'   , csrf_exempt(FirstnameValidation.as_view()), name=''),
    path('validate-mname'   , csrf_exempt(UsernameValidation.as_view()) , name=''),
]

