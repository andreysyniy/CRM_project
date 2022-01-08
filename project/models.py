from django.db import models
from django.db.models.fields import CharField, DateTimeField
from tinymce import models as tinymce_models


class Project(models.Model):
  '''Модель Проект'''
  name = CharField('Проект', max_length=100)
  description = tinymce_models.HTMLField('Описание')
  date_begin = DateTimeField('Дата начала',auto_now=False, auto_now_add=False)
  date_end = DateTimeField('Дата окончания', auto_now=False, auto_now_add=False)
  price = models.DecimalField('Стоимость', max_digits=10, decimal_places=0, default=0)
  client = models.ForeignKey('client.Client', on_delete=models.CASCADE, related_name='client_project')

  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Проект'
    verbose_name_plural = 'Проекты'


