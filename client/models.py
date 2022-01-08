from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField
from django.urls import reverse
from tinymce import models as tinymce_models



class Email(models.Model):
  '''Модель email'''
  email = EmailField('Электронная почта', max_length=100)
  client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, related_name='client_emails')

  def __str__(self):
      return self.email

  class Meta:
    verbose_name = 'Электронная почта'
    verbose_name_plural = 'Электронная почта'


class Phone(models.Model):
  '''Модель телефон'''
  phone = CharField('Телефон', max_length=50)
  client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, related_name='client_phones')

  def __str__(self):
      return self.phone

  class Meta:
    verbose_name = 'Телефон'
    verbose_name_plural = 'Телефоны'


class Client(models.Model):
  '''Модель клиент'''
  company_name = CharField('Название компании', max_length=100)
  full_name_director = CharField('Ф.И.О. директора', max_length=100)
  short_description = tinymce_models.HTMLField('Краткое описание')
  date_create = DateTimeField('Дата создания',auto_now_add=True)
  date_change = DateTimeField('Дата изменения', auto_now=True)
  address = CharField('Адрес', max_length=200)

  def __str__(self):
      return self.company_name

  def get_absolute_url(self):
    return reverse('client_detail', kwargs={'client_id': self.pk})  

  class Meta:
    verbose_name = 'Клиент'
    verbose_name_plural = 'Клиенты'
    ordering = ['company_name', 'date_create']

