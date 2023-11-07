from .modules.error_pages.views_error_404                       import error_page_404
from .modules.auth.views_registry                               import registry
# from .modules.auth.views_login                                import log_in
# from .modules.auth.views_logout                               import logout
from .modules.acad_head.dashboard.views_exec_dashboard          import exec_dashboard
from .modules.acad_head.evaluations.views_exec_evalupload       import evaluations
from .modules.acad_head.evaluations.views_exec_evaluation       import eval_analytics
from .modules.maintenance.views_comesoon                        import coming_soon
from .modules.acad_head.profile.views_exec_profilepage          import exec_p_page
from .modules.acad_head.profile.views_exec_profilesetting       import exec_p_sett
from .modules.acad_head.pro_dev.views_exec_prodev               import prdv_wrkshp_att
from .modules.acad_head.pro_dev.views_exec_prodev_analytics      import prdv_wrkshp_anl
# from .modules.acad_head.attend_leave.views_exec_alm_attendance  import alm_attendance_rec
from .modules.acad_head.attend_leave.views_exec_alm_leaves      import alm_leaves_rec
from .modules.acad_head.attend_leave.views_exec_alm_analytics   import alm_analytics
from .modules.acad_head.awards_recog.views_exec_awards          import awards_recog

# Authentication
registry
# log_in
# logout

# Errors
error_page_404

# Acad_Head
exec_dashboard
evaluations
eval_analytics

exec_p_page
exec_p_sett

prdv_wrkshp_att
prdv_wrkshp_anl

# alm_attendance_rec
alm_leaves_rec
alm_analytics

awards_recog

# Maintenance
coming_soon
