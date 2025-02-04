# Student Management App (DRF)
A simple Django Rest Framework application to manage student data. This application provides CRUD functionality for students' information like name, enrollment_date, course, gender,etc.

## Features
- Add a new student.
- View details of all students.
- Edit student details.
- Delete a student.

## Installation Steps
1.	Create a Virtual Environment (if not already created):
   `python -m venv venv`
2.	Activate the Virtual Environment:
    `venv\Scripts\activate`
3.	Install Django:
     `pip install Django`
4.	Create a Django Project:
    `django-admin startproject myproject`
    `cd myproject`
5.	Create a Django App:
   `python manage.py startapp myapp`
6.	Configure Database
7.	Migrate the Database: `python manage.py migrate`
8.	Run the Development Server:
`python manage.py runserver`

## Requirements
- PostgreSQL (or any other database of your choice)
- asgiref==3.8.1
- certifi==2024.12.14
- charset-normalizer==3.4.1
- coreapi==2.3.3
- coreschema==0.0.4
- Django==5.1.4
- djangorestframework==3.15.2
- drf-yasg==1.21.8
- Faker==33.3.1
- idna==3.10
- inflection==0.5.1
- itypes==1.2.0
- Jinja2==3.1.5
- MarkupSafe==3.0.2
- packaging==24.2
- python-dateutil==2.9.0.post0
- pytz==2024.2
- PyYAML==6.0.2
- requests==2.32.3
- ruamel.yaml==0.18.10
- ruamel.yaml.clib==0.2.12
- six==1.17.0
- sqlparse==0.5.3
- typing_extensions==4.12.2
- tzdata==2024.2
- uritemplate==4.1.1
- urllib3==2.3.0
