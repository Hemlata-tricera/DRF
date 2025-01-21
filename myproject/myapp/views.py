# from django.shortcuts import render
from .models import Student
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer, StudentQueryParamSerializer
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q




@swagger_auto_schema(
    method='get',
    query_serializer=StudentQueryParamSerializer
)
@api_view(['GET'])
def student_list_view(request):
    # students = Student.objects.all()
    # data = {
    #     'students': list(students.values())
    serializer = StudentQueryParamSerializer(data=request.GET)
    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data)
    first_name = serializer.validated_data.get('first_name')
    last_name = serializer.validated_data.get('last_name')

    # Get all students
    students = Student.objects.all()
    print(students)

    if first_name and last_name:
        students = students.filter(Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name))

    serializer = StudentSerializer(students, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def student_detail_view(request, id):
    try:
        student = Student.objects.get(student_id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        raise NotFound(detail="Student not found")  # Handling the case when student doesn't exist






