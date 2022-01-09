from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from project.models import Project
from client.models import Client


class ProjectList(ListView):
  '''Отображение списка проектов'''
  model = Project
  paginate_by = 4
  template_name = 'project/project_list.html'
  context_object_name = 'project_list'
  extra_context = {'title': 'Все проекты'}

  def get_ordering(self):
      return self.request.GET.get('orderby')


class ProjectClientList(DetailView):
  '''Отображение списка проектов для конкретного клиента'''
  model = Client
  template_name = 'project/project_client_list.html'
  pk_url_kwarg = 'client_id'
  extra_context = {'title': 'Проекты клиента'}
  allow_empty = True

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['project_client_list'] = Project.objects.filter(client_id=self.kwargs['client_id'])
      return context


class ProjectDetail(DetailView):
  model = Project
  template_name = 'project/project_detail.html'
  pk_url_kwarg = 'project_id'
  context_object_name = 'project_detail'
  extra_context = {'title': 'Информация о проекте'}


class ProjectCreate(CreateView):
  '''Форма создания проекта'''  
  model = Project
  fields = '__all__'
  template_name = 'project/project_create.html'
  pk_url_kwarg = 'project_id'
  success_url = reverse_lazy('project_list')
  extra_context = {'title': 'Создание проекта'}



class ProjectUpdate(UpdateView):
  '''Форма редактирования проекта'''  
  model = Project
  fields = '__all__'
  template_name = 'project/project_update.html'
  pk_url_kwarg = 'project_id'
  success_url = reverse_lazy('project_list')
  extra_context = {'title': 'Редактирование проекта'}


class ProjectDelete(DeleteView):
  '''Форма удаления проекта'''  
  model = Project
  fields = '__all__'
  template_name = 'project/project_delete.html'
  pk_url_kwarg = 'project_id'
  success_url = reverse_lazy('project_list')
  extra_context = {'title': 'Удаление проекта'}
