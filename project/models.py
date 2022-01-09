from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.urls.base import reverse
from tinymce import models as tinymce_models


class Project(models.Model):
  '''Модель Проект'''
  name = CharField('Проект', max_length=100)
  description = tinymce_models.HTMLField('Описание')
  date_begin = DateTimeField(verbose_name='Дата начала',auto_now=False, auto_now_add=False)
  date_end = DateTimeField(verbose_name='Дата окончания', auto_now=False, auto_now_add=False)
  price = models.DecimalField(verbose_name='Стоимость', max_digits=10, decimal_places=0, default=0)
  client = models.ForeignKey('client.Client', on_delete=models.CASCADE, related_name='project_client', verbose_name='Клиент')

  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Проект'
    verbose_name_plural = 'Проекты'

  def get_absolute_url(self):
    return reverse('project_detail', kwargs={'project_id': self.pk})  

