from .modules.error_pages.views_error_404 import error_page_404
from .modules.auth.views_registry import RegistryView
from .modules.auth.views_login import LoginView
from .modules.auth.views_logout import logout
from .modules.acad_head.dashboard.views_exec_dashboard import exec_dashboard
from .modules.acad_head.evaluations.views_exec_evalupload import evaluations
from .modules.acad_head.evaluations.views_exec_evaluation import eval_analytics
from .modules.maintenance.views_comesoon import coming_soon
from .modules.acad_head.profile.exec_profilepage import exec_p_page
from .modules.acad_head.profile.exec_profilesetting import exec_p_sett

# Authentication
RegistryView
LoginView
logout

# Errors
error_page_404

# Acad_Head
exec_dashboard
evaluations
eval_analytics
exec_p_page
exec_p_sett

# Maintenance
coming_soon
