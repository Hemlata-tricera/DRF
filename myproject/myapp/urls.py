from django.urls import path, include
from .import views
# from .views import StudentAPI
from .views import StudentGeneric,StudentGeneric1
from rest_framework.routers import DefaultRouter
# Create a router and register our ViewSets with it.
router = DefaultRouter()

# router.register(r'students', views.StudentViewSet, basename='student') # ModelViewSet Endpoint
# router.register(r'students', views.StudentReadOnlyViewSet, basename='student') # ReadOnlyViewSet Endpoint

urlpatterns=[
     # path('', include(router.urls)),  # for router
     path('generic-student/', StudentGeneric.as_view()),
     path('generic-student/<int:student_id>/', StudentGeneric1.as_view()),


     #URLS FOR APIVIEWSSET
     # path('students/', views.StudentListAPI.as_view(), name='student-list'),
     # path('students/<int:pk>/', views.StudentDetailAPI.as_view(), name='student-detail')

     # path('students/', views.student_list_view, name='student_list'),
    # # path('GET /students/?first_name=Hemlata', views.student_list_view, name='student_list'),
    # path('get/students-details/<str:id>/', views.student_detail_view, name='student_detail'),
    # path('post/students/', views.student_create_view, name='create-student'),  # Create student endpoint
    # path('students/<int:student_id>/',  views.student_update_view, name='update-student'),
    # path('delete/students/<int:student_id>/',  views.student_delete_view, name='delete-student'),

]