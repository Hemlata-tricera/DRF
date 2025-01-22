# from django.shortcuts import render
from .models import Student
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer, StudentQueryParamSerializer, StudentCreateSerializer
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q
from django.shortcuts import get_object_or_404





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




# @swagger_auto_schema(
#     method='POST',
#     request_body=StudentSerializer,
#     responses={201: StudentSerializer}  # Successful response will return a serialized Student object
# )
# @api_view(['POST'])
# def student_create_view(request):
#     serializer = StudentSerializer(data=request.data)
#     print(serializer.validated_data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@swagger_auto_schema(
    method='POST',
    request_body=StudentCreateSerializer,
    responses={201: StudentCreateSerializer}  # Successful response will return a serialized Student object
)
@api_view(['POST'])
def student_create_view(request):
    serializer = StudentCreateSerializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data)
    serializer.save()
    return Response({'payload': serializer.data, 'message': 'Students added successfully', 'status': 201})
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='PUT',
    request_body=StudentSerializer,
    responses={201: StudentSerializer}  # Successful response will return a serialized Student object
)
@api_view(['PUT'])
def student_update_view(request, student_id):

    student = get_object_or_404(Student, student_id=student_id)

    # Deserialize the incoming data and pass the student instance to update
    serializer = StudentSerializer(student, data=request.data)

    # Check if the data is valid
    serializer.is_valid(raise_exception=True)
    # Save the updated student instance
    serializer.save()

    # Return a response with the updated student data
    return Response(serializer.data, status=status.HTTP_200_OK)









