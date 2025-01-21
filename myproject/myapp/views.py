# from django.shortcuts import render
from .models import Student
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.exceptions import NotFound



@api_view(['GET'])
def student_list_view(request):
    # students = Student.objects.all()
    # data = {
    #     'students': list(students.values())
    #         }
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def student_detail_view(request, id):
    try:
        student = Student.objects.get(student_id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        raise NotFound(detail="Student not found")  # Handling the case when student doesn't exist



# def student_detail_view(request, pk):
#     student = Student.objects.get(pk=pk)
#     data = {
#         'name': student.name,
#         'email': student.email
#     }
#     return JsonResponse(data)





