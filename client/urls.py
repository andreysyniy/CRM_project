from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('client/<int:client_id>/', ClientDetail.as_view(), name='client_detail'),
    path('clientedit/<int:client_id>/', ClientEdit.as_view(), name = 'client_edit'),
]

