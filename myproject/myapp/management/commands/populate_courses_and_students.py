from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import Student, Course
from django.utils import timezone
import random
import uuid



class Command(BaseCommand):
    help = 'Populate the Student and Course models with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create sample courses
        course_names = ['Math 101', 'Science 101', 'History 101', 'Computer Science 101', 'Literature 101']
        for name in course_names:
            Course.objects.get_or_create(name=name, code=f"{fake.random_int(100, 999)}")

        # Get all courses from the database
        courses = Course.objects.all()

        for _ in range(50):  # Create 50 students
            # Generate fake data for the student
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone_number = fake.phone_number()
            address = fake.address()
            dob = fake.date_of_birth(minimum_age=18, maximum_age=30)  # Random DOB for 18-30 years old
            enrollment_date = fake.date_this_decade()  # Enrollment date within the last 10 years
            gender = random.choice(['Male', 'Female', 'Other'])  # Random gender
            student_id = f"STU-{str(uuid.uuid4()).split('-')[0].upper()}"

            # Create the student record
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address=address,
                dob=dob,
                enrollment_date=enrollment_date,
                gender=gender,
                student_id=student_id
            )

            # Assign 1 to 3 random courses to the student
            num_courses = random.randint(1, 3)
            random_courses = random.sample(list(courses), num_courses)
            student.courses.add(*random_courses)  # Assign the selected courses to the student

        self.stdout.write(self.style.SUCCESS('Successfully populated 50 students and courses'))
