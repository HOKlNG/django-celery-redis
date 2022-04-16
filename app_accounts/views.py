from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import check_password, make_password
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.views.generic.edit import FormView,View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site

from app_accounts.forms import UserForm, LoginForm
from app_accounts.task import task_send_register_mail
from app_accounts.models import User
from app_accounts.tokens import activate_token

# Create your views here.
def index(request):
    return HttpResponse('test')

# 회원가입
class CreateAccounts(FormView):
    template_name = 'register.html'
    form_class = UserForm
    success_url = '/accounts/signin'

    def form_valid(self, form):
        password = make_password(form.data.get('password'))
        user = User(
            email=form.data.get('email'),
            password=password,
            nickname=form.data.get('nickname'),
        )
        user.is_active = False
        user.save()

        #회원 가입 이메일 전송송
        task_send_register_mail.delay(user.pk, get_current_site(self.request).__str__())

        return super().form_valid(form)

#로그인 페이지
class LoginPage(FormView):
    # 로그인 페이지 View
    template_name = 'login.html'
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
        return redirect('/main')

class LogOutView(View):

    def get(self, request):
        logout(request)
        request.session.pop('login', None)
        return redirect('/accounts/signin')

def activate(request):
    uidb64 = request.GET.get('uidb64')
    token = request.GET.get('token')


    uid = force_text(urlsafe_base64_decode(uidb64))
    user = get_object_or_404(User, pk=uid)

    user = User.objects.get(pk=uid)

    #활성화 인증
    if user is not None and activate_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('signin_page')
    else:
        return HttpResponse('비정상적인 접근입니다.')