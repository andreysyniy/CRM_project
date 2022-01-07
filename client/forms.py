from django import forms
from .models import *
from tinymce.widgets import TinyMCE
from django.http import request


class ClientCreateForm(forms.Form):
  company_name = forms.CharField(label='Название Компании', widget=forms.TextInput())
  full_name_director = forms.CharField(label='Ф.И.О.', widget=forms.TextInput())
  short_description = forms.CharField(label='Краткое Описание' ,widget=TinyMCE(attrs={'cols': 50, 'rows': 20}))
  address = forms.CharField(label='Адрес', widget=forms.TextInput())
  # class Meta:
  #   model = Client
  #   fields = '__all__'  
  

# class ClientUpdateForm(forms.Form):
#   company_name = forms.CharField(label='Название Компании', widget=forms.TextInput())
#   full_name_director = forms.CharField(label='Ф.И.О.', widget=forms.TextInput())
#   short_description = forms.CharField(label='Краткое Описание' ,widget=TinyMCE(attrs={'cols': 50, 'rows': 20}))
#   address = forms.CharField(label='Адрес', widget=forms.TextInput())
#   phone = forms.CharField(label='Телефон', widget=forms.TextInput())
#   email = forms.EmailField(label='Электронная почта', widget=forms.TextInput())
  


# class ClientUpdateForm(forms.ModelForm):
#   class Meta:
#     model = Client
#     fields = ['company_name', 'full_name_director', 'short_description', 'address']

#     # widgets = {
#     #   'company_name': forms.TextInput(attrs={'class': 'form-control'}),
#     #   'full_name_director': forms.TextInput(attrs={'class': 'form-control'}),
#     #   'short_description': forms.TextInput(attrs={'class': 'form-control'}),
#     # }

#     class Media:
#         js = ('/site_media/static/tiny_mce/tinymce.min.js',)

# class ClientPhoneUpdateForm(forms.ModelForm):
#   class Meta:
#     model = Phone
#     fields = ['phone']

# class ClientEmailUpdateForm(forms.ModelForm):
#   class Meta:
#     model = Email
#     fields = ['email']



