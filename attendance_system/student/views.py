from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from student.models import Student
from teacher.models import Teacher
from attendance.models import Attendance
from leave.models import LeaveRequest
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm
# Create your views here.



def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_register.html', {'form': form})

def student_dashboard(request):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        attendance_records = Attendance.objects.filter(student=student)
        return render(request, 'student_dashboard.html', {'attendance_records': attendance_records})
    return redirect('login')