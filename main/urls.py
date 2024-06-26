from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tournament/', views.tournament, name='tournament'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
]
