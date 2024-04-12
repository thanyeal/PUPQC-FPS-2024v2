from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .validate import EmailValidation, PasswValidation, LogEmailValidation, LogPasswValidation, LastnameValidation, FirstnameValidation, UsernameValidation
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #for error pages
    path('error_404'        , views.error_page_404  , name="error_page_404" ),
    path('error_500'        , views.error_page_500  , name="error_page_500" ),

    #for acad head
    path(''                 , views.exec_dashboard  , name="exec_dashboard" ),
    path('dashboard'        , views.exec_dashboard  , name="exec_dashboard" ),
    
    path('eval_upload'      , views.evaluations     , name="eval_upload"    ),
    path('eval_analytics'   , views.eval_analytics  , name="eval_analytics" ),
    path('eval_list'        , views.eval_list       , name="eval_list"      ),
    
    path('exec_profile'     , views.exec_p_page     , name="exec_profile"   ),
    path('exec_settings'    , views.exec_p_sett     , name="exec_settings"  ),

    path('prodev_attendance', views.prdv_wrkshp_att   , name="prodev_attendance" ),
    path('prodev_analytics' , views.prdv_wrkshp_anl   , name="prodev_analytics"  ),

    path('attendance_leaves', views.alm_leaves_rec    , name="attendance_leaves" ),
    path('alm_analytics'    , views.alm_analytics     , name="alm_analytics"     ),

    path('awards_recog'     , views.awards_recog      , name="awards_recog"      ),
    path('awards_analytics' , views.awards_analytics  , name="awards_analytics"  ),

    # path('retentions'       , views.retention_insights   , name="retentions"     ),
    # path('ret_analytics'    , views.retention_analytics  , name="ret_analytics"  ),

    path("mrt_promotion"    , views.mrt_promote     , name="mrt_promotion"  ),
    path("mrt_analytics"    , views.mrt_analytics   , name="mrt_analytics"  ),

    # path("fac_contents"     , views.fac_contents     , name="fac_contents"  ),
    # path("fac_analytics"    , views.fac_analytics    , name="fac_analytics" ),

    path("rsrch_analytics"      , views.rsrch_analytics   , name="rsrch_analytics"  ),
    path("rsrch_tracking"       , views.rsrch_tracking    , name="rsrch_tracking"   ),
    # path("rsrch_generate_pdf"   , views.rsrch_generate_pdf, name="rsrch_generate_pdf"),

    path("workload_dat"         , views.workload_dat        , name="workload_dat"       ),
    path("workload_analytics"   , views.workload_analytics  , name="workload_analytics" ),

    # for maintenance page
    path('coming_soon'      , views.coming_soon     , name="coming_soon"),

    # for Faculty Management Page
    path('fac_mgmnt'     , views.fac_mgmnt    , name="fac_mgmnt"),
    path('faculty_info'  , views.faculty_info , name="faculty_info"),
    path('faculty_indiv_report'  , views.faculty_indiv_report , name="faculty_indiv_report"),
    path('faculty_mgmt_reports'  , views.faculty_mgmt_reports , name="faculty_mgmt_reports"),
    path('faculty_proc_data'  , views.faculty_proc_data , name="faculty_proc_data"),

    # for log and reg page
    path('registry/'        , views.registry        , name="registry"   ),
    path('login'   , auth_views.LoginView.as_view() , name="login"      ),
    path('logout/', views.custom_logout, name='logout'),

    # for validation view for labels in the form
    path('validate-email'   , csrf_exempt(EmailValidation.as_view())    , name=''),
    path('validate-passw'   , csrf_exempt(PasswValidation.as_view())    , name=''),
    path('validate-webmail' , csrf_exempt(LogEmailValidation.as_view()) , name=''),
    path('validate-webpass' , csrf_exempt(LogPasswValidation.as_view()) , name=''),
    path('validate-lname'   , csrf_exempt(LastnameValidation.as_view()) , name=''),
    path('validate-fname'   , csrf_exempt(FirstnameValidation.as_view()), name=''),
    path('validate-mname'   , csrf_exempt(UsernameValidation.as_view()) , name=''),

    path('ris/', views.testresearchinfodata),
    path('fis/', views.testfacultyinfodata),

    path('testpage', views.testfunct),
]

