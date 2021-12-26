from django.contrib import admin
from django.db import models
from .models import Client, Email, Phone

# Register your models here.


class PhoneInline(admin.TabularInline):
  model = Phone
  extra = 0


class EmailInline(admin.TabularInline):
  model = Email
  extra = 0


class ClientAdmin(admin.ModelAdmin):
  list_display = ('company_name', 'full_name_director', 'date_create', 'date_change', 'address', 'short_description')
  inlines = [PhoneInline, EmailInline]


admin.site.register(Client, ClientAdmin)
admin.site.register(Email)
admin.site.register(Phone)
