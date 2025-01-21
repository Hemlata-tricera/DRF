from django.contrib import admin
from .models import Student, Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'dob', 'gender')


admin.site.register(Student, StudentAdmin)
admin.site.register(Course)