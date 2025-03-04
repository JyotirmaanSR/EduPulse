from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from student.models import Student
from teacher.models import Teacher
from attendance.models import Attendance
from leave.models import LeaveRequest
from django.contrib.auth.decorators import login_required
from .forms import TeacherRegistrationForm
# Create your views here.


def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_register.html', {'form': form})

def teacher_dashboard(request):
    if request.user.is_authenticated:
        teacher = Teacher.objects.get(user=request.user)
        students = Student.objects.filter(subjects=teacher.subject)
        leave_requests = LeaveRequest.objects.filter(teacher=teacher)
        return render(request, 'teacher_dashboard.html', {'students': students, 'subject': teacher.subject, 'leave_requests': leave_requests})
    return redirect('login')

def apply_leave(request):
    if request.method == 'POST':
        date = request.POST['date']
        reason = request.POST['reason']
        teacher = Teacher.objects.get(user=request.user)
        LeaveRequest.objects.create(teacher=teacher, date=date, reason=reason)
    return redirect('teacher_dashboard')
