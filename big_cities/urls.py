"""big_cities URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from user_app import views
#from templates import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration_form/',views.registration_form_view,name='registration_form'),
    url(r'^city_form/',views.city_form_view,name='city_form'),
    url(r'^article_form/',views.article_form_view,name='article_form'),
    url(r'^organization_form/',views.organization_form_view,name='organization_form'),
    url(r'^tag_form/',views.tag_form_view,name='tag_form'),
    url(r'^home_page/',views.home_page_view,name='home_page'),
    url(r'^user_profile/',views.user_profile_view,name='user_profile')
]
