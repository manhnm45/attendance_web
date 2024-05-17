from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from employees import views as employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def get_home(request):
#     return render(request, 'home.html')

def get_home(request):
    return render(request, 'home.html')
def do_login(request):
    print("request.user.is_authenticated",request.user.is_authenticated)
    if request.user.is_authenticated:
        return HttpResponse('home_holder')
    print("method",request.method)
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request , username= username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home_holder'))
        else: 
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponseRedirect(reverse('home'))


def home_holder(request):
    return render(request, "home_holder.html")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
def check_list_staff(request):
    return HttpResponseRedirect(reverse('employee'))

