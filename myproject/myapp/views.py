# from django.shortcuts import render
from .models import Student, Course
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer, StudentQueryParamSerializer, StudentCreateSerializer, StudentCreate_newSerializer
from django.http import Http404
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapigit
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .custompermissions import Mypermission






#USING Mixins
# ListModelMixin and CreateModelMixin
class CreateListStudents(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    authentication_classes = [SessionAuthentication]
    permission_classes = [Mypermission]


class RetrieveUpdateDeleteIStudent(mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
#Trying to create custom mixing//incomplete//ignore
# class MyRetrieveCreateAPIView(mixins.RetrieveModelMixin,mixins.CreateModelMixin,GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'student_id'
#
#
#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)





#USING Generic Views
# class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
# class StudentGeneric1(generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'student_id'


#USING VIEWSET
# class StudentViewSet(viewsets.ViewSet):
#     queryset = Student.objects.all()
#
#     def list(self, request):
#         # students = Student.objects.all()
#         serializer = StudentSerializer(self.queryset, many=True)
#         return Response(serializer.data)
#
#     @swagger_auto_schema(request_body=StudentSerializer,operation_description="Create a new Student")
#     def create(self, request):
#          serializer = StudentSerializer(data=request.data)
#          serializer.is_valid(raise_exception=True)
#          serializer.save()
#          return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         student = get_object_or_404(self.queryset, pk=pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     @swagger_auto_schema(request_body=StudentSerializer,operation_description="Update a Student")
#     def update(self, request, pk):
#         student = get_object_or_404(self.queryset, pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
#     @swagger_auto_schema(request_body=StudentSerializer, tags=["Students"])
#     def partial_update(self, request, pk):
#         """ Partial update"""
#         student = get_object_or_404(self.queryset, pk=pk)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
#     def destroy(self, request, pk):
#         student = get_object_or_404(self.queryset, pk=pk)
#         student.delete()
#         return Response(request.data)
#



#USING MODELVIEWSET
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# USING ReadOnlyModelViewSet
# class StudentReadOnlyViewSet(ReadOnlyModelViewSet):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
#


























# Added two different API view classes for LIST view and DETAIL view
# to improve the understanding of Swagger for better API documentation.

# class StudentListAPI(APIView):
#     @swagger_auto_schema(responses={200: StudentSerializer(many=True)})
#     def get(self, request, format=None):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     @swagger_auto_schema(request_body=StudentSerializer,operation_description="Create a new Student")
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#
#         if serializer.is_valid():
#             # print(serializer.validated_data)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # For GET request: Use manual_parameters to define query parameters
#     # @swagger_auto_schema(manual_parameters=[
#     #     openapi.Parameter('first_name', openapi.IN_QUERY, description="Filter by first name", type=openapi.TYPE_STRING),
#     #     openapi.Parameter('last_name', openapi.IN_QUERY, description="Filter by last name", type=openapi.TYPE_STRING),
#     # ])
#     # def get(self, request):
#     #     serializer = StudentQueryParamSerializer(data=request.GET)
#     #     serializer.is_valid(raise_exception=True)
#     #     print(serializer.validated_data)
#     #     first_name = serializer.validated_data.get('first_name')
#     #     last_name = serializer.validated_data.get('last_name')
#     #
#     #     # Get all students
#     #     students = Student.objects.all()
#     #     print(students)
#     #
#     #     if first_name and last_name:
#     #         students = students.filter(Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name))
#     #
#     #     serializer = StudentSerializer(students, many=True)
#     #     print(serializer.data)
#     #     return Response(serializer.data)
#
# class StudentDetailAPI(APIView):
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             raise Http404
#
#     @swagger_auto_schema(responses={200: StudentSerializer})
#     def get(self, request, pk, format=None):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     @swagger_auto_schema(request_body=StudentSerializer,operation_description="Update a Student")
#     def put(self, request, pk, format=None):
#         student = self.get_object(pk)
#
#          # Deserialize the incoming data and pass the student instance to update
#         serializer = StudentSerializer(student, data=request.data)
#
#         # Check if the data is valid
#         serializer.is_valid(raise_exception=True)
#         # Save the updated student instance
#         serializer.save()

#         # Return a response with the updated student data
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @swagger_auto_schema(request_body=StudentSerializer,operation_description="Partial Update a Student")
#     def patch(self, request, pk):
#         student = get_object_or_404(Student, student_id=pk)
#
#         # Deserialize the incoming data and pass the student instance to update
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#
#            # Check if the data is valid
#         serializer.is_valid(raise_exception=True)
#             # Save the updated student instance
#         serializer.save()
#
#         # Return a response with the updated student data
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         student = get_object_or_404(Student, student_id=pk)
#         student.delete()
#         return Response({'message': f'Student with id {pk}  has been deleted successfully'
#         },status=status.HTTP_200_OK)
#
#
#
#









#CODE FOR FUNCTION BASE VIEW USING @api_view decorator
# @swagger_auto_schema(
#     method='get',
#     query_serializer=StudentQueryParamSerializer
# )
# @api_view(['GET'])
# def student_list_view(request):
#     # students = Student.objects.all()
#     # data = {
#     #     'students': list(students.values())
#     serializer = StudentQueryParamSerializer(data=request.GET)
#     serializer.is_valid(raise_exception=True)
#     print(serializer.validated_data)
#     first_name = serializer.validated_data.get('first_name')
#     last_name = serializer.validated_data.get('last_name')
#
#     # Get all students
#     students = Student.objects.all()
#     print(students)
#
#     if first_name and last_name:
#         students = students.filter(Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name))
#
#     serializer = StudentSerializer(students, many=True)
#     print(serializer.data)
#     return Response(serializer.data)


# @api_view(['GET'])
# def student_detail_view(request, id):
#     try:
#         student = Student.objects.get(student_id=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#     except Student.DoesNotExist:
#         raise NotFound(detail="Student not found")  # Handling the case when student doesn't exist
#


#Create view with .save() metthod
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



#create view without .save() method
# @swagger_auto_schema(
#     method='POST',
#     request_body=StudentCreate_newSerializer,
#     responses={201: StudentCreate_newSerializer}  # Successful response will return a serialized Student object
# )
# @api_view(['POST'])
# def student_create_view(request):
#     serializer = StudentCreate_newSerializer(data=request.data)
#
#     serializer.is_valid(raise_exception=True)
#     # print(serializer.validated_data)
#     # serializer.save()
#     # return Response({'payload': serializer.data, 'message': 'Students added successfully', 'status': 201})
#     student_data = serializer.validated_data
#     student = Student.objects.create(
#         first_name=student_data['first_name'],
#         last_name=student_data['last_name'],
#         dob=student_data['dob'],
#         email=student_data['email'],
#         address=student_data['address'],
#         phone_number=student_data['phone_number'],
#         enrollment_date=student_data['enrollment_date'],
#         gender=student_data['gender'],
#         # courses_id=student_data['courses']
#
#     )
#     if 'courses' in student_data:
#         courses = Course.objects.filter(id__in=student_data['courses'])
#         student.courses.set(courses)
#     return Response({'payload': StudentCreate_newSerializer(student).data, 'message': 'Students added successfully', 'status': 201})
#     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @swagger_auto_schema(
#     method='PUT',
#     request_body=StudentSerializer,
#     responses={201: StudentSerializer}  # Successful response will return a serialized Student object
# )
# @api_view(['PUT'])
# def student_update_view(request, student_id):
#
#     student = get_object_or_404(Student, student_id=student_id)
#
#     # Deserialize the incoming data and pass the student instance to update
#     serializer = StudentSerializer(student, data=request.data)
#
#     # Check if the data is valid
#     serializer.is_valid(raise_exception=True)
#     # Save the updated student instance
#     serializer.save()
#
#     # Return a response with the updated student data
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# @swagger_auto_schema(
#     method='PATCH',
#     request_body=StudentSerializer,
#     responses={201: StudentSerializer}  # Successful response will return a serialized Student object
# )
# @api_view(['PATCH'])
# def student_update_view(request, student_id):
#
#     student = get_object_or_404(Student, student_id=student_id, partial=True)
#
#     # Deserialize the incoming data and pass the student instance to update
#     serializer = StudentSerializer(student, data=request.data)
#
#     # Check if the data is valid
#     serializer.is_valid(raise_exception=True)
#     # Save the updated student instance
#     serializer.save()
#
#     # Return a response with the updated student data
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#
# @swagger_auto_schema(
#     method='DELETE',
#     request_body=StudentSerializer,
#     responses={201: StudentSerializer}  # Successful response will return a serialized Student object
# )
# @api_view(['DELETE'])
# def student_delete_view(request, student_id):
#
#     student = get_object_or_404(Student, student_id=student_id)
#     student.delete()
#     return Response({'message': f'Student with id {student_id}  has been deleted successfully'
# },status=status.HTTP_200_OK)
#
#
#
#
#
#





