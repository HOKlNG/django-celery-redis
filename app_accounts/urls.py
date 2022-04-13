from django.urls import path
from app_accounts.views import index, CreateAccounts

urlpatterns = [
    path('', index),
    path('signup', CreateAccounts.as_view(), name='signup')
]