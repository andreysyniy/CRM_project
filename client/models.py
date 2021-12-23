from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField
from django.urls import reverse

# Create your models here.

class Email(models.Model):
  email = EmailField(max_length=100)
  client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)

  def __str__(self):
      return self.email

  class Meta:
    verbose_name = 'Электронная почта'
    verbose_name_plural = 'Электронная почта'


class Phone(models.Model):
  phone = CharField(max_length=50)
  client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)

  def __str__(self):
      return self.phone

  class Meta:
    verbose_name = 'Телефон'
    verbose_name_plural = 'Телефоны'


class Client(models.Model):
  company_name = CharField('Название компании', max_length=100)
  full_name_director = CharField('Ф.И.О. директора', max_length=100)
  short_description = TextField('Краткое описание', max_length=300)
  date_create = DateTimeField('Дата создания',auto_now_add=True)
  date_change = DateTimeField('Дата изменения', auto_now=True)
  address = CharField('Адрес', max_length=200)

  def __str__(self):
      return self.company_name

  # def get_absolute_url(self):
  #   return reverse('client', kwargs={'client_id': self.pk})  

  class Meta:
    verbose_name = 'Клиент'
    verbose_name_plural = 'Клиенты'
    ordering = ['company_name', 'date_create']