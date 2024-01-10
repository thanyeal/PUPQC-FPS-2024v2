from .modules.error_pages.views_error_404                         import error_page_404
from .modules.auth.views_registry                                 import registry
from .modules.auth.views_logout                                   import custom_logout
from .modules.acad_head.dashboard.views_exec_dashboard            import exec_dashboard
from .modules.acad_head.evaluations.views_exec_evalupload         import evaluations
from .modules.acad_head.evaluations.views_exec_evaluation         import eval_analytics
from .modules.maintenance.views_comesoon                          import coming_soon
from .modules.acad_head.profile.views_exec_profilepage            import exec_p_page
from .modules.acad_head.profile.views_exec_profilesetting         import exec_p_sett
from .modules.acad_head.pro_dev.views_exec_prodev                 import prdv_wrkshp_att
from .modules.acad_head.pro_dev.views_exec_prodev_analytics       import prdv_wrkshp_anl
from .modules.acad_head.attend_leave.views_exec_alm_leaves        import alm_leaves_rec
from .modules.acad_head.attend_leave.views_exec_alm_analytics     import alm_analytics
from .modules.acad_head.awards_recog.views_exec_awards            import awards_recog
from .modules.acad_head.awards_recog.views_exec_awards_analytics  import awards_analytics
from .modules.acad_head.retention_exits.views_exec_rt_anl         import retention_analytics
from .modules.acad_head.retention_exits.views_exec_rt_ins         import retention_insights
from .modules.acad_head.merit_prmot.views_exec_mrt_promotion      import mrt_promote
from .modules.acad_head.merit_prmot.views_exec_mrt_analytics      import mrt_analytics
from .modules.acad_head.feedbacks.views_exec_feedback_comms       import fac_contents
from .modules.acad_head.feedbacks.views_exec_feedback_analytics   import fac_analytics
from .modules.acad_head.research.views_exec_research              import rsrch_tracking
from .modules.acad_head.research.views_exec_research_analytics    import rsrch_analytics
from .modules.acad_head.workload.views_exec_workload              import workload_dat
from .modules.acad_head.workload.views_exec_workload_analytics    import workload_analytics

# Authentication
registry
# log_in
custom_logout

# Errors
error_page_404

# Acad_Head
exec_dashboard
evaluations
eval_analytics

# Profile
exec_p_page
exec_p_sett

# Research Publication
rsrch_analytics
rsrch_tracking

# Professional Development
prdv_wrkshp_att
prdv_wrkshp_anl

# Attendance Leave Management
alm_analytics
alm_leaves_rec

# Retention Exit
retention_analytics
retention_insights

# Faculty
fac_analytics
fac_contents

# Merit Promotions
mrt_analytics
mrt_promote

# Workloads
workload_dat
workload_analytics

# Awards and Recognition
awards_analytics
awards_recog

# Maintenance
coming_soon
