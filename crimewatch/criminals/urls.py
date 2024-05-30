from django.urls import path
from . import views

urlpatterns = [
    path('', views.criminal_list, name='criminal_list'),
    path('create/', views.criminal_create, name='criminal_create'),
    path('update/<int:pk>/', views.criminal_update, name='criminal_update'),
    path('delete/<int:pk>/', views.criminal_delete, name='criminal_delete'),
    path('female-criminals/', views.female_criminals_list, name='female_criminals_list'),
    path('male-criminals/', views.male_criminals_list, name='male_criminals_list'),
]
