from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<int:client_id>/', ClientDetail.as_view(), name='client_detail'),
    path('create/', ClientCreate.as_view(), name = 'client_create'),
    path('update/<int:client_id>/', ClientUpdate.as_view(), name = 'client_update'),
    path('delete/<int:client_id>/', ClientDelete.as_view(), name = 'client_delete'),
]

home_patterns = [
    path('', ClientList.as_view(), name='client_list'),
]