from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import FormView,View
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from app_accounts.forms import UserForm, LoginForm

class MainPage(View):

    template_name = 'index.html'
    def get(self, request, **kwargs):
        return render(request, self.template_name)

# Create your views here.
def dashboard(request):
    return render(request, template_name='dashboard.html')