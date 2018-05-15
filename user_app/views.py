from django.shortcuts import render
from . import forms

def index(request):
    return render(request,'forms/index.html')

def registration_form_view(request):
    form = forms.RegistrationForm()
    return render(request,'forms/registration_form.html',{'form':form})

# Create your views here.
