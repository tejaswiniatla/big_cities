from django import forms

class RegistrationForm(forms.Form):
    Firstname = forms.CharField()
    Lastname = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()

class CityForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    title = forms.CharField()
    link_to_pdf = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    user_id = forms.IntegerField()

class OrganizationForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
    address = forms.CharField()
    cityID = forms.IntegerField()

class TagForm(forms.Form):
    id = forms.IntegerField()
    keyword = forms.CharField()

class HomePage(forms.Form):
    city_name = forms.CharField()
    org_name = forms.CharField()
