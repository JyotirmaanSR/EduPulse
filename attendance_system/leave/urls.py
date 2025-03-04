from django.urls import path
from .views import admin_dashboard, approve_leave, reject_leave

urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('approve-leave/<int:leave_id>/', approve_leave, name='approve_leave'),
    path('reject-leave/<int:leave_id>/', reject_leave, name='reject_leave'),
]
