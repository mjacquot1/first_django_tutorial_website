from django.urls import path
from . import views

# Register the app namespace so that URLS can be found in views
# app_name is a django variable
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
    path('db_list/', views.db_list_view, name='db_list')
]
