from django.contrib import admin
from .models import Project

# class ProjectAdmin(admin.ModelAdmin):
#   list_display = ('company_name', 'full_name_director', 'date_create', 'date_change', 'address', 'short_description')
#   inlines = [PhoneInline, EmailInline]


# admin.site.register(Client, ClientAdmin)

admin.site.register(Project)
