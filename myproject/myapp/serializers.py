from rest_framework import serializers
# from datetime import date
from .models import Student, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'code']


class StudentSerializer(serializers.ModelSerializer):
    # We use the CourseSerializer to handle ManyToManyField
    # courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'email', 'phone_number','address', 'enrollment_date', 'courses', 'gender', 'student_id']

    def create(self, validated_data):
        # Extract courses from validated data (assuming it is a list of course ids)
        courses_data = validated_data.pop('courses', [])
        student = Student.objects.create(**validated_data)
        print(student)
        # Now associate the courses with the student (if any courses are provided)
        if courses_data:
            print(courses_data)
            student.courses.set(courses_data)  # Assign courses to the student


        return student

class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ['courses']

class StudentCreate_newSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'email', 'address', 'phone_number', 'enrollment_date', 'gender', 'courses']




class StudentQueryParamSerializer(serializers.Serializer):

         first_name = serializers.CharField(max_length=100)
         last_name = serializers.CharField(max_length=100)

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
