from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('clientes/', views.clientes, name='clientes'),
    path('ver_cliente/<int:id>', views.ver_cliente, name='ver_cliente'),
    
]