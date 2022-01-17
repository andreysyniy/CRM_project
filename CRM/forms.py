from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PersonalInfoForm(forms.Form):
 username = forms.CharField(max_length=50, label='Имя пользователя', help_text= 'Только латинские буквы')
 first_name = forms.CharField(max_length=50)
 last_name = forms.CharField(max_length=50, required=False)
 email = forms.EmailField()

class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=100, required=True, label='Имя')
  last_name = forms.CharField(max_length=100, required=True, label='Фамилия')
  email = forms.EmailField(max_length=250, help_text='youremail@mail.com', label='Электронная почта')

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')
