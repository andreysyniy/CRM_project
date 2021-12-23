# from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.

# def home(request):
#   client_info = Client.objects.all()
#   return render(request, 'client/home.html', {'client_info': client_info,'title': 'Домашняя страница'})

class Home(ListView):
  model = Client
  # paginate_by = 2
  template_name = 'client/home.html'
  context_object_name = 'client_info'
  extra_context = {'title': 'Домашняя страница'}

  def get_ordering(self):
      return self.request.GET.get('orderby')