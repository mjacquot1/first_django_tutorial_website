from django.urls import path  # Needed for paths to work
from . import views  # Import all views

app_name = 'cars'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
]
