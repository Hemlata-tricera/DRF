from django.shortcuts import render
from .models import Student, Course
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def student_list_view(request):
    students = Student.objects.all()
    data = {
        'students': list(students.values())
            }
    return Response(data)


def student_detail_view(request, pk):
    student = Student.objects.get(pk=pk)
    data = {
        'name': student.name,
        'email': student.email
    }
    return JsonResponse(data)



