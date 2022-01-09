from django.contrib import admin
from django.urls import path, include
from project.urls import prj_cli_list_patterns
from client.urls import home_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_patterns)),
    path('client/', include('client.urls')),
    path('project/', include('project.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include(prj_cli_list_patterns)),
]
