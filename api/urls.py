
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='products'),
    path('allowed-hosts/', allowed_hosts, name='allowed-hosts'),

]
