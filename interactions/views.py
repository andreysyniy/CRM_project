from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from client.models import Client
from project.models import Project
from .models import Interaction

class InteractionsForClients(ListView):
  '''Отображение взаимодействий для всех клиентов'''
  pass


class InteractionsForProjects(ListView):
  '''Отображение взаимодействий для всех проектов'''
  pass


class InteractionsForClient(DetailView):
  '''Отображение взаимодействий для одного клиента'''
  model = Client
  paginate_by = 4
  template_name = 'interactions/interactions_client.html'
  pk_url_kwarg = 'client_id'
  extra_context = {'title': 'Взаимодействия по клиенту'}
  allow_empty = True

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['interactions_client_list'] = Interaction.objects.filter(client_id=self.kwargs['client_id']).order_by(self.request.GET.get('orderby', 'project'))
    return context

class InteractionsForProject(DetailView):
  '''Отображение взаимодействий для одного проекта'''
  model = Project
  paginate_by = 4
  template_name = 'interactions/interactions_project.html'
  pk_url_kwarg = 'project_id'
  extra_context = {'title': 'Взаимодействия по проекту'}
  allow_empty = True

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['interactions_project_list'] = Interaction.objects.filter(project_id=self.kwargs['project_id']).order_by(self.request.GET.get('orderby', 'project'))
    return context


class InteractionDetail(DetailView):
  '''Отображение детальное отображение информации взаимодействия'''
  pass


class InteractionCreate(CreateView):
  '''Создание нового взаимодействия'''
  pass


class InteractionUpdate(UpdateView):
  '''Редактирование взаимодействия'''
  pass


class InteractionDelete(DeleteView):
  '''Удаление взаимодействия'''
  pass
