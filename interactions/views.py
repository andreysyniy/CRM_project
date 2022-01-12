from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from client.models import Client
from project.models import Project
from .models import Interaction

class InteractionsList(ListView):
  '''Отображение взаимодействий для всех клиентов'''
  model = Interaction
  paginate_by = 4
  template_name = 'interactions/interactions_list.html'
  extra_context = {'title': 'Взаимодействия'}

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['interactions_list'] = Interaction.objects.all().order_by(self.request.GET.get('orderby', 'project'))
    return context


class InteractionDetail(DetailView):
  '''Отображение детальное отображение информации взаимодействия'''
  model = Interaction
  fields = '__all__'
  template_name = 'interactions/interaction_detail.html'
  pk_url_kwarg = 'interaction_id'
  context_object_name = 'interaction_detail'
  # success_url = reverse_lazy('interactions_list')
  extra_context = {'title': 'Информация о взаимодействии'}


class InteractionCreate(CreateView):
  '''Создание нового взаимодействия'''
  model = Interaction
  fields = '__all__'
  template_name = 'interactions/interaction_create.html'
  # pk_url_kwarg = 'interaction_id'
  success_url = reverse_lazy('interactions_list')
  extra_context = {'title': 'Создание взаимодействия'}


class InteractionUpdate(UpdateView):
  '''Редактирование взаимодействия'''
  model = Interaction
  fields = '__all__'
  template_name = 'interactions/interaction_update.html'
  pk_url_kwarg = 'interaction_id'
  success_url = reverse_lazy('interactions_list')
  extra_context = {'title': 'Обновление взаимодействия'}



class InteractionDelete(DeleteView):
  '''Удаление взаимодействия'''
  model = Interaction
  fields = '__all__'
  template_name = 'interactions/interaction_delete.html'
  pk_url_kwarg = 'interaction_id'
  success_url = reverse_lazy('interactions_list')
  extra_context = {'title': 'Удаление взаимодействия'}