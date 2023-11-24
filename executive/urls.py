from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .validate import EmailValidation, PasswValidation, LogEmailValidation, LogPasswValidation, LastnameValidation, FirstnameValidation, UsernameValidation
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #for error pages
    path('error'            , views.error_page_404  , name="error_page_404"),

    #for acad head
    path(''                 , views.exec_dashboard  , name="exec_dashboard" ),
    path('dashboard'        , views.exec_dashboard  , name="exec_dashboard" ),
    
    path('eval_upload'      , views.evaluations     , name="eval_upload"    ),
    path('eval_analytics'   , views.eval_analytics  , name="eval_analytics" ),
    
    path('exec_profile'     , views.exec_p_page     , name="exec_profile"   ),
    path('exec_settings'    , views.exec_p_sett     , name="exec_settings"  ),

    path('prodev_attendance', views.prdv_wrkshp_att   , name="prodev_attendance" ),
    path('prodev_analytics' , views.prdv_wrkshp_anl   , name="prodev_analytics"  ),

    path('attendance_leaves', views.alm_leaves_rec    , name="attendance_leaves" ),
    path('alm_analytics'    , views.alm_analytics     , name="alm_analytics"     ),

    path('awards_recog'     , views.awards_recog      , name="awards_recog"      ),

    path('retentions'       , views.retention_insights   , name="retentions"     ),
    path('ret_analytics'    , views.retention_analytics  , name="ret_analytics"  ),

    path("mrt_promotion"    , views.mrt_promote     , name="mrt_promotion"  ),
    path("mrt_analytics"    , views.mrt_analytics   , name="mrt_analytics"  ),

    path("fac_contents"     , views.fac_contents     , name="fac_contents"  ),
    path("fac_analytics"    , views.fac_analytics    , name="fac_analytics" ),

    path("rsrch_analytics"  , views.rsrch_analytics   , name="rsrch_analytics"  ),
    path("rsrch_tracking"   , views.rsrch_tracking    , name="rsrch_tracking"   ),

    # for maintenance page
    path('coming_soon'      , views.coming_soon     , name="coming_soon"),

    # for log and reg page
    path('registry/'        , views.registry        , name="registry"   ),
    path('login'   , auth_views.LoginView.as_view() , name="login"      ),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'     ),

    # for validation view for labels in the form
    path('validate-email'   , csrf_exempt(EmailValidation.as_view())    , name=''),
    path('validate-passw'   , csrf_exempt(PasswValidation.as_view())    , name=''),
    path('validate-webmail' , csrf_exempt(LogEmailValidation.as_view()) , name=''),
    path('validate-webpass' , csrf_exempt(LogPasswValidation.as_view()) , name=''),
    path('validate-lname'   , csrf_exempt(LastnameValidation.as_view()) , name=''),
    path('validate-fname'   , csrf_exempt(FirstnameValidation.as_view()), name=''),
    path('validate-mname'   , csrf_exempt(UsernameValidation.as_view()) , name=''),
]
