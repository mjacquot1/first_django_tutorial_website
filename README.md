# first_django_tutorial_website

test

Is this working now too?

* Creating Project
Create Project 
- django-admin startproject <project_name>
Create App (if needed)
- cd <project_name>
- python manage.py startapp <app_name>
Create 'views.py' in app
Import 'include' in <project_name>/urls.py from 'from django.urls import'
Add <project_name>/urls.py 'urlpatterns'
- path('my_app', include('my_app.urls')),
Migrate with python manage.py migrate
Add app to <project_name>/settings.py by adding '<app_name>.settings.<AppName>Config' to the 'INSTALLED_APPS' list.
Run 'python manage.py makemigrations <app_name>'
Templates must be in a folder named 'templates' for django to look for them there
