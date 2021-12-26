# from django.shortcuts import render
from django.views.generic.edit import CreateView

from client.forms import ClientEditForm
from .models import *
from django.views.generic import ListView, DetailView

# Create your views here.

# def home(request):
#   client_info = Client.objects.all()
#   return render(request, 'client/home.html', {'client_info': client_info,'title': 'Домашняя страница'})

class Home(ListView):
  '''Отображение списка клиентов'''
  model = Client
  paginate_by = 2
  template_name = 'client/home.html'
  context_object_name = 'client_info'
  extra_context = {'title': 'Домашняя страница'}

  def get_ordering(self):
      return self.request.GET.get('orderby')


# def detail_info(request, client_id):
#   return HttpResponse(f"Client {client_id}")

# class ClientDetail(ListView):
#   model = Client
#   template_name = 'client/client.html'
#   context_object_name = 'client_detail'
#   extra_context = {'title': 'Детальная информация'}

#   def get_queryset(self):
#     return Client.objects.filter(id=self.kwargs['client_id']).first

class ClientDetail(DetailView):
  '''Детальная информация о клиенте'''
  model = Client
  template_name = 'client/client.html'
  pk_url_kwarg = 'client_id'
  context_object_name = 'client_detail'


class ClientEdit(CreateView):
  '''Форма редактирования клиентской информации'''
  form_class = ClientEditForm
  template_name = 'client/client_edit.html'

