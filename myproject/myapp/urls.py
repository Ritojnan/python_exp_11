from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('students/', views.students, name='students'),
]