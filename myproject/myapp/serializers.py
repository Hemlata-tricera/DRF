from rest_framework import serializers
# from datetime import date
from .models import Student, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'code']


class StudentSerializer(serializers.ModelSerializer):
    # We use the CourseSerializer to handle ManyToManyField
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'email', 'phone_number','address', 'enrollment_date', 'courses', 'gender', 'student_id']


# class StudentSerializer(serializers.Serializer):
#     # first_name = serializers.CharField(max_length=100)
#     # last_name = serializers.CharField(max_length=100, allow_blank=True)
#     # dob = serializers.DateField(default='2000-01-01')
#     # email = serializers.EmailField()
#     # phone_number = serializers.CharField(max_length=15, allow_blank=True)
#     # address = serializers.CharField(style={'base_template': 'textarea.html'},allow_blank=True)
#     # enrollment_date = serializers.DateField(default=date.today)
#     # courses = serializers.ListField(child=serializers.IntegerField(), required=False)  # Use ListField for related course IDs
#     # gender = serializers.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=False)
#     # student_id = serializers.CharField(max_length=20)
