from django.urls import path
from app_main import views

urlpatterns = [
    path('', views.dashboard, name='main'),
]