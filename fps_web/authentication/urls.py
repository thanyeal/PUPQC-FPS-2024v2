from .views import LoginView
from django.urls import path

urlpatterns = [
    path('', LoginView.as_view(), name="login")
]
