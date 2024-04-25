from executive.modules.error_pages.views_error_404                         import error_page_404
from executive.modules.error_pages.views_error_500                         import error_page_500
from executive.modules.auth.views_registry                                 import registry
from executive.modules.auth.views_logout                                   import custom_logout
from executive.modules.maintenance.views_comesoon                          import coming_soon
from executive.modules.acad_head.profile.views_exec_profilepage            import exec_p_page
from executive.modules.acad_head.profile.views_exec_profilesetting         import exec_p_sett
from executive.modules.auth.views_login                                    import CustomLoginView

from executive.modules.acad_head.dashboard._views    import db_asView
from executive.modules.acad_head.faculties._views    import fm_asView, fn_asView, fo_asView, fp_asView
from executive.modules.acad_head.evaluates._views    import el_asView, em_asView
from executive.modules.acad_head.research._views     import rs_asView, rt_asView
from executive.modules.acad_head.pro_dev._views      import pd_asView, pe_asView
from executive.modules.acad_head.ranking._views      import pr_asView

db_asView

fm_asView
fn_asView
fo_asView
fp_asView

el_asView
em_asView

rs_asView
rt_asView

pd_asView
pe_asView

pr_asView



# Authentication
CustomLoginView
registry
custom_logout

# Errors
error_page_404
error_page_500

# Profile
exec_p_page
exec_p_sett

# Maintenance
coming_soon