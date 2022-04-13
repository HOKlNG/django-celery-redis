from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic import CreateView

from app_accounts.forms import UserForm


# Create your views here.
def index(request):
    return HttpResponse('test')

# 회원가입
class CreateAccounts(CreateView):
    template_name = 'signup.html'
    form_class = UserForm
    success_url = '/accounts'

