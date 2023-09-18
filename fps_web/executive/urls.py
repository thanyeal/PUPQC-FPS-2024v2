from django.urls import path
from . import views

urlpatterns = [
    path('', views.exec_dashboard, name="exec_dashboard"),
    path('evaluations', views.evaluations, name="evaluations")
]
