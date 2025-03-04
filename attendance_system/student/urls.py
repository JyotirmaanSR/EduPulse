from django.urls import path
from .views import student_dashboard,student_register

urlpatterns = [
    path('dashboard/', student_dashboard, name='student_dashboard'),
     path('register/', student_register, name='student_register'),
]
