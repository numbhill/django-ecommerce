from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_summary, name='cart'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]