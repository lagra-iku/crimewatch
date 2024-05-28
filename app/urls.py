from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('case/new/', views.case_new, name='case_new'),
    path('register_officer', views.register_officers, name='register_officers'),
    path('list', views.case_list, name='case_list'),
    path('case/<int:pk>/', views.case_detail, name='case_detail'),
    
    path('case/<int:pk>/edit/', views.case_edit, name='case_edit'),
]