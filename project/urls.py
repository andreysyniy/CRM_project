from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ProjectList.as_view(), name = 'project_list'),
    path('detail/<int:project_id>/', ProjectDetail.as_view(), name = 'project_detail'),
    path('create/', ProjectCreate.as_view(), name = 'project_create'),
    path('update/<int:project_id>/', ProjectUpdate.as_view(), name = 'project_update'),
    path('delete/<int:project_id>/', ProjectDelete.as_view(), name = 'project_delete'),
]

prj_cli_list_patterns = [
    path('client/<int:client_id>/project/list/', ProjectClientList.as_view(), name = 'project_client_list'),
]