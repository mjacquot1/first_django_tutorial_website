"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http.response import HttpResponse #An http response object.

# Add the abilityo to include the urls.py file from first_app
from django.conf.urls import include

# # Add views from first_app
# from first_app import views

# from local folder import views
from . import views

urlpatterns = [
    path('', views.home_view , name='home'),
    path('admin/', admin.site.urls),
    path('firstapp/', include('first_app.urls')), # Get all the first_app urls under firstapp/
    # path('hello/', views.index, name='index'), # Return the views.index view in first_app/views
]
