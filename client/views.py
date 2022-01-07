from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from client.forms import ClientCreateForm
from .models import *
from django.views.generic import ListView, DetailView


class Home(ListView):
  '''Отображение списка клиентов'''
  model = Client
  paginate_by = 2
  template_name = 'client/home.html'
  context_object_name = 'client_list'
  extra_context = {'title': 'Домашняя страница'}

  def get_ordering(self):
      return self.request.GET.get('orderby')


class ClientDetail(DetailView):
  '''Детальная информация о клиенте'''
  model = Client
  template_name = 'client/client_detail.html'
  pk_url_kwarg = 'client_id'
  context_object_name = 'client_detail'


class ClientCreate(FormView):
  '''Форма редактирования клиентской информации'''
  form_class = ClientCreateForm
  template_name = 'client/client_create.html'
  success_url = reverse_lazy('home')

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Создание информации о клиенте'
      return context



# class ClientUpdate(View):
#   '''Форма редактирования клиентской информации'''
#   def get(self, request, client_id):
#     phone_list = dict()
#     client = Client.objects.get(pk__iexact = client_id)
#     phone = Phone.objects.filter(client_id = client_id)
#     for i in range(len(phone)):
#       print(i)
#       phone_list['phone'] = phone[i].phone
#     print(phone_list)
#     bound_form = ClientUpdateForm(initial=model_to_dict(client) | phone_list)
#     return render(request, 'client/client_update.html', context={'form': bound_form, 'client': client})
    
  # form_class = ClientUpdateForm
  # # fields = ['company_name', 'full_name_director', 'short_description', 'address']
  # template_name = 'client/client_update.html'
  # # pk_url_kwarg = 'client_id'


  # def get_context_data(self, **kwargs):
  #     context = super().get_context_data(**kwargs)
  #     context['phone_list'] = Phone.objects.filter(client_id = 1)
  #     context['email_list'] = Email.objects.filter(client_id = 1)
  #     context['title'] = 'Обновление информации о клиенте'
  #     return context


# def client_update_func(request, client_id):
#   client = Client.objects.get(pk=client_id)
#   # PhoneFormset = modelformset_factory(Phone, fields=('phone',))
#   PhoneFormset = inlineformset_factory(Client, Phone, fields=('phone',), can_delete=True, extra=1)
#   EmailFormset = inlineformset_factory(Client, Email, fields=('email',), can_delete=True, extra=1)

#   if request.method == 'POST':
#     # formset = PhoneFormset(request.POST, queryset=Phone.objects.filter(client__id=client.id))
#     phone_formset = PhoneFormset(request.POST, instance=client)
#     email_formset = EmailFormset(request.POST, instance=client)
#     if phone_formset.is_valid() and email_formset.is_valid():
#       phone_formset.save()
#       email_formset.save()
#       # instances = formset.save(commit=False)
#       # for instance in instances:
#       #   instance.client_id = client.id
#       #   instance.save()
      
      
#       return redirect('client_detail', client_id=client.id)

#   # formset = PhoneFormset(queryset=Phone.objects.filter(client__id=client.id))

#   phone_formset = PhoneFormset(instance=client)
#   email_formset = EmailFormset(instance=client)

  
#   return render(request, 'client/client_update.html', {'phone_formset' : phone_formset, 'email_formset' : email_formset})



class ClientUpdate(UpdateView):
  '''Форма редактирования клиентской информации'''  
  fields = ['company_name', 'full_name_director', 'short_description', 'address']
  model = Client
  template_name = 'client/client_update.html'
  pk_url_kwarg = 'client_id'
  # context_object_name = 'client_info'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['second_model'] = Phone.objects.filter(client__id=self.kwargs['client_id'])
    return context




class ClientDelete(DeleteView):
  '''Форма редактирования клиентской информации'''
  model = Client
  fields = ['company_name', 'full_name_director', 'short_description', 'address']
  template_name = 'client/client_update.html'
  pk_url_kwarg = 'client_id'

class PhoneUpdate(UpdateView):
  '''Форма редактирования клиентской информации'''
  model = Phone
  fields = ['phone']
  template_name = 'client/client_update.html'
  pk_url_kwarg = 'client_id'


class EmailUpdate(UpdateView):
  '''Форма редактирования клиентской информации'''
  model = Email
  fields = ['email']
  template_name = 'client/client_update.html'
  pk_url_kwarg = 'client_id'
