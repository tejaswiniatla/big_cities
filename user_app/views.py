from django.shortcuts import render
from . import forms

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
# Create your views here.
