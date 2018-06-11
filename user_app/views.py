from django.shortcuts import render
from . import forms
from .models import User

def index(request):
    return render(request,'forms/index.html')

def registration_form_view(request):
    form = forms.RegistrationForm()
    return render(request,'forms/registration_form.html',{'form':form})

def city_form_view(request):
    form = forms.CityForm()
    return render(request,'forms/city_form.html',{'form':form})

def article_form_view(request):
    form = forms.ArticleForm()
    return render(request,'forms/article_form.html',{'form':form})

def organization_form_view(request):
    form = forms.OrganizationForm()
    return render(request,'forms/organization_form.html',{'form':form})

def tag_form_view(request):
    form = forms.TagForm()
    return render(request,'forms/tag_form.html',{'form':form})

def home_page_view(request):
    form = forms.HomePage()
    return render(request,'forms/home_page.html',{'form':form})

def user_profile_view(request,user_name):
    name_list = user_name
    return render(request,'forms/user_profile.html',{'User':user})

# Create your views here.
