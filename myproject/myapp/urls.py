from django.urls import path
from .import views

urlpatterns=[
    path('list', views.student_list_view, name='student_list'),
    path('<int:id>', views.student_detail_view, name='student_detail'),



]