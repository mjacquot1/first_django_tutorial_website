from django.shortcuts import render
from django.http.response import HttpResponse #An http response object.

# Create a view here for home.
def home_view(request):
    return HttpResponse("<h1>HOME PAGE</h1>")