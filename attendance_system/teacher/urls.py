from django.urls import path
from .views import teacher_dashboard, apply_leave,teacher_register

urlpatterns = [
    path('dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('apply-leave/', apply_leave, name='apply_leave'),
    path('register/', teacher_register, name='teacher_register'),
]
