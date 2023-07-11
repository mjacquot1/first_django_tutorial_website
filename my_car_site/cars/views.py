from django.shortcuts import render, redirect
from django.urls import reverse

from . import models

# Create your views here.


def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request, 'cars/list.html', context=context)


def add(request):
    # Check to see if the request being sent is a 'post' request from submission
    if request.POST:
        brand = request.POST['brand']
        year = request.POST['year']
        models.Car.objects.create(brand=brand, year=year)
        # If user submited new car go to 'list.html'
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')


def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            redirect(reverse('cars:list'))
        except:
            print(f'pk:{pk} not found')
            redirect(reverse('cars:list'))
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')
