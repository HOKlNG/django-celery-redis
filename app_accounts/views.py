from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import FormView,View
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from app_accounts.forms import UserForm, LoginForm


# Create your views here.
def index(request):
    return HttpResponse('test')

# 회원가입
class CreateAccounts(CreateView):
    template_name = 'signup.html'
    form_class = UserForm
    success_url = '/accounts'

#로그인 페이지
class LoginPage(FormView):
    # 로그인 페이지 View
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('accounts_main')

#로그인 시도
class LoginView(View):

    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password',None)
        #인증증
        user = authenticate(request, email=email, password=password)
        #정보 불일치
        if user is None:
            pass
        #로그인
        login(request, user)
        return JsonResponse({'msg':'success signin'}, status=200)

class LogOutView(View):

    def get(self, request):
        logout(request)
        request.session.pop('login', None)
        return redirect('/')