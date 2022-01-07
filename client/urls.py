from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('client_detail/<int:client_id>/', ClientDetail.as_view(), name='client_detail'),
    path('client_create/', ClientCreate.as_view(), name = 'client_create'),
    path('client_update/<int:client_id>/', ClientUpdate.as_view(), name = 'client_update'),
    path('client_delete/<int:client_id>/', ClientDelete.as_view(), name = 'client_delete'),
]

