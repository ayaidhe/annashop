from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),  # Ajout de cette ligne
    path('add/', views.cart_add, name='cart_add'),
    path('summary/', views.cart_summary, name='cart_summary'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('update/', views.cart_update, name='cart_update'),
]

