from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.models import User, Group
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from CRM.forms import PersonalInfoForm


class PersonalInfo(ListView):
  '''Отображение списка клиентов'''
  model = User
  fields = ('__all__')
  template_name = 'registration/personal.html'
  context_object_name = 'personal'
  extra_context = {'title': 'Личный кабинет'}

def personal_info(request):
  form = PersonalInfoForm()
  form.initial['username'] = 'User Andrey'
  form.initial['first_name'] = 'Andrey'
  form.initial['email'] = 'andreysyn@mail.ru'
  if request.method == 'POST':
    print(request.POST)
    form = PersonalInfoForm(request.POST)
    if form.is_valid():
      print('form is valid')
      print(form.cleaned_data)
  context = {'form': form, 'title': 'Персональная информация'}
  return render(request, 'registration/personal_info.html', context=context)

def signUpView(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      print(form.cleaned_data)
      signup_user = User.objects.get(username=username)
      user_group = Group.objects.get(name='User')
      user_group.user_set.add(signup_user)
      return redirect('success_signup')
  else:
    form = SignUpForm()
  return render(request, 'registration/signup.html', {'form': form})


def logInView(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('client_list')
      else:
        return redirect('signup')

  else:
    form = AuthenticationForm()
  return render(request, 'registration/login.html', {'form': form, 'title': 'Вход'})


def signoutView(request):
  logout(request)
  return redirect('login')


def successSignUpView(request):
  return render(request, 'registration/success_signup.html', {'title': 'Успешная регистрация'})