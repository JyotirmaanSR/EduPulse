from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from student.models import Student, Subject
from teacher.models import Teacher
from attendance.models import Attendance
from leave.models import LeaveRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
def mark_attendance(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        subject_id = request.POST['subject_id']
        status = request.POST['status'] == 'Present'
        student = Student.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)
        Attendance.objects.create(student=student, subject=subject, status=status)
    return redirect('teacher_dashboard')


