from django.urls import path
from . import views

urlpatterns = [
    path('', views.criminal_list, name='criminal_list'),
    path('create/', views.criminal_create, name='criminal_create'),
    path('update/<int:pk>/', views.criminal_update, name='criminal_update'),
    path('delete/<int:pk>/', views.criminal_delete, name='criminal_delete'),
]
