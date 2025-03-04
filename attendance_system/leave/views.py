from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from student.models import Student
from teacher.models import Teacher
from attendance.models import Attendance
from leave.models import LeaveRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
def admin_dashboard(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'admin_dashboard.html', {'leave_requests': leave_requests})

def approve_leave(request, leave_id):
    leave_request = LeaveRequest.objects.get(id=leave_id)
    leave_request.status = 'Approved'
    leave_request.save()
    return redirect('admin_dashboard')

def reject_leave(request, leave_id):
    leave_request = LeaveRequest.objects.get(id=leave_id)
    leave_request.status = 'Rejected'
    leave_request.save()
    return redirect('admin_dashboard')