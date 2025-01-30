from django.urls import path, include
from .import views
# from .views import StudentAPI
from rest_framework.routers import DefaultRouter
# Create a router and register our ViewSets with it.
# router = DefaultRouter()
# router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns=[
     # path('', include(router.urls)),

     path('students/', views.StudentAPI.as_view()),
     # path('students/<int:pk>/', views.StudentAPI.as_view()),

     # path('students/', views.student_list_view, name='student_list'),
    # # path('GET /students/?first_name=Hemlata', views.student_list_view, name='student_list'),
    # path('get/students-details/<str:id>/', views.student_detail_view, name='student_detail'),
    # path('post/students/', views.student_create_view, name='create-student'),  # Create student endpoint
    # path('students/<int:student_id>/',  views.student_update_view, name='update-student'),
    # path('delete/students/<int:student_id>/',  views.student_delete_view, name='delete-student'),

]