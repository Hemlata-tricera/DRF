from django.urls import path
from .import views
# from .views import StudentAPI

urlpatterns=[
     path('students/', views.StudentAPI.as_view()),
     path('students/<int:pk>/', views.StudentAPI.as_view()),

     # path('students/', views.student_list_view, name='student_list'),
    # # path('GET /students/?first_name=Hemlata', views.student_list_view, name='student_list'),
    # path('get/students-details/<str:id>/', views.student_detail_view, name='student_detail'),
    # path('post/students/', views.student_create_view, name='create-student'),  # Create student endpoint
    # path('students/<int:student_id>/',  views.student_update_view, name='update-student'),
    # path('delete/students/<int:student_id>/',  views.student_delete_view, name='delete-student'),

]