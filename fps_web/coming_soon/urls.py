from .views import ComingSoonView
from django.urls import path

urlpatterns = [
    path('coming_soon', ComingSoonView.as_view(), name="coming_soon")
]
