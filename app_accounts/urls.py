from django.urls import path
from app_accounts.views import index, CreateAccounts, LoginView, LoginPage, LogOutView

urlpatterns = [
    path('', index, name='accounts_main'),
    path('signup', CreateAccounts.as_view(), name='register'),
    path('signin', LoginPage.as_view(), name='signin_page'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogOutView.as_view(), name='logout')
]