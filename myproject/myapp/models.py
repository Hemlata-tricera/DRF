from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True, default=101)


    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(null=False, blank=False, default='2025-01-01')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True, null=True, blank=True)
    courses = models.ManyToManyField('Course', blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
                              blank=True, null=True)
    student_id = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Unique student ID

    def __str__(self):
        return self.first_name