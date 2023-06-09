from django.shortcuts import render
from django.http import HttpResponse #An http response object.

# Create your views here.

# Each view requires a function
# Each view must return an http response object.
def index(request): #Call it "request" as convention
    return HttpResponse("<em> My Second App </em>")


# Create your views here.
