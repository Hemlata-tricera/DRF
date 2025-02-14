from django.urls import path, include
# from .import views
# from .views import StudentAPI
# from .views import StudentGeneric,StudentGeneric1, CreateListStudents
from .views import CreateListStudents, RetrieveUpdateDeleteIStudent
from rest_framework.routers import DefaultRouter
# Create a router and register our ViewSets with it.
router = DefaultRouter()
# from rest_framework.authtoken.views import obtain_auth_token
# from myapp.auth import CustomAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView



# router.register(r'students', views.StudentViewSet, basename='student') # ModelViewSet Endpoint
# router.register(r'students', views.StudentReadOnlyViewSet, basename='student') # ReadOnlyViewSet Endpoint

urlpatterns=[
     # path('', include(router.urls)),  # for router
     # path('generic-student/', StudentGeneric.as_view()), #Generic View
     # path('generic-student/<int:student_id>/', StudentGeneric1.as_view()), #Generic View
     path('mixins-students/', CreateListStudents.as_view()),  # Generic View
     path('mixins-student/<int:student_id>/', RetrieveUpdateDeleteIStudent.as_view()), #Generic View
     # path('student/<int:student_id>/', MyRetrieveCreateAPIView.as_view()), #Generic View
     # path('gettoken/', obtain_auth_token, name='api_token_auth'),
     # path('gettoken/', CustomAuthToken.as_view(), name='CustomAuthToken'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get access & refresh token
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

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