from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from numpy import logical_not, require
from .forms import PhoneFormset, EmailFormset, CreateEmailFormset, CreatePhoneFormset
from .models import *
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# class ClientList(LoginRequiredMixin, ListView):
class ClientList(ListView):
  '''Отображение списка клиентов'''
  # login_url = '/login/'
  # redirect_field_name = 'redirect_to'
  model = Client
  paginate_by = 4
  template_name = 'client/client_list.html'
  context_object_name = 'client_list'
  extra_context = {'title': 'Список клиентов'}

  def get_ordering(self):
      return self.request.GET.get('orderby')


class ClientDetail(DetailView):
  '''Детальная информация о клиенте'''
  model = Client
  template_name = 'client/client_detail.html'
  pk_url_kwarg = 'client_id'
  context_object_name = 'client_detail'
  extra_context = {'title': 'Информация о клиенте'}


class ClientCreate(CreateView):
  '''Форма создания клиента'''
  model = Client
  fields = '__all__'
  template_name = 'client/client_create.html'
  success_url = reverse_lazy('client_list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Создание клиента'
    if self.request.POST:
        context['phone_formset'] = CreatePhoneFormset(self.request.POST, instance=self.object)
        context['phone_formset'].full_clean()
        
        context['email_formset'] = CreateEmailFormset(self.request.POST, instance=self.object)
        context['email_formset'].full_clean()
    else:
        context['phone_formset'] = CreatePhoneFormset(instance=self.object)
        context['email_formset'] = CreateEmailFormset(instance=self.object)
    return context

  def form_valid(self, form):
    context = self.get_context_data(form=form)
    phone_formset = context['phone_formset']
    email_formset = context['email_formset']
    if phone_formset.is_valid() and email_formset.is_valid():
      response = super().form_valid(form)
      phone_formset.instance = self.object
      phone_formset.save()
      email_formset.instance = self.object
      email_formset.save()
      return response
    else:
      return super().form_invalid(form)




class ClientUpdate(UpdateView):
  '''Форма редактирования клиента'''  
  model = Client
  fields = '__all__'
  template_name = 'client/client_update.html'
  pk_url_kwarg = 'client_id'
  success_url = reverse_lazy('client_list')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Редактирование клиента'
    if self.request.POST:
        context['phone_formset'] = PhoneFormset(self.request.POST, instance=self.object)
        context['phone_formset'].full_clean()
        
        context['email_formset'] = EmailFormset(self.request.POST, instance=self.object)
        context['email_formset'].full_clean()
    else:
        context['phone_formset'] = PhoneFormset(instance=self.object)
        context['email_formset'] = EmailFormset(instance=self.object)
    return context

  def form_valid(self, form):
    context = self.get_context_data(form=form)
    phone_formset = context['phone_formset']
    email_formset = context['email_formset']
    if phone_formset.is_valid() and email_formset.is_valid():
      response = super().form_valid(form)
      phone_formset.instance = self.object
      phone_formset.save()
      email_formset.instance = self.object
      email_formset.save()
      return response
    else:
      return super().form_invalid(form)


class ClientDelete(DeleteView):
  '''Форма удаления клиента'''
  model = Client
  fields = ['company_name', 'full_name_director', 'short_description', 'address']
  pk_url_kwarg = 'client_id'
  template_name = 'client/client_delete.html'
  success_url = reverse_lazy('client_list')
  extra_context = {'title': 'Удаление клиента'}

