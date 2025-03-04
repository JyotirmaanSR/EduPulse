from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from student.models import Student, Subject
from teacher.models import Teacher
from attendance.models import Attendance
from leave.models import LeaveRequest
from django.contrib.auth.decorators import login_required



# Authentication Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'student'):
                return redirect('student_dashboard')
            elif hasattr(user, 'teacher'):
                return redirect('teacher_dashboard')
        return render(request, 'login.html', {'error': 'Invalid Credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')