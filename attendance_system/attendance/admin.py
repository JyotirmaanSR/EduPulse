from django.contrib import admin
from student.models import Student
from teacher.models import Teacher
from attendance.models import Attendance, Subject
from leave.models import LeaveRequest

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(LeaveRequest)