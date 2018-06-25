from django.contrib import admin
from .models import Staff, Student, Attendance, Subject
# Register your models here.
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Subject)
