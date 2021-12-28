from django import forms
from tinymce.widgets import TinyMCE
from .models import *

class ClientEditForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = ['company_name', 'full_name_director', 'short_description']

    widgets = {
      'company_name': forms.TextInput(attrs={'class': 'form-control'}),
      'full_name_director': forms.TextInput(attrs={'class': 'form-control'}),
      'short_description': forms.TextInput(attrs={'class': 'form-control'}),
    }

    class Media:
        js = ('/site_media/static/tiny_mce/tinymce.min.js',)
