from django.shortcuts import render
from .models import Student, Course
from django.http import JsonResponse
# Create your views here.


def student_list_view(request):
    students = Student.objects.all()
    data = {
        'students': list(students.values())
    }
    return JsonResponse(data)

def student_detail_view(request, pk):
    student = Student.objects.get(pk=pk)
    data = {
        'name': student.name,
        'email': student.email
    }
    return JsonResponse(data)



