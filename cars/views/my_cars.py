from django.shortcuts import render
from cars.models import Car

def my_cars(request):
    
    if request.user.is_authenticated:
        cars = Car.objects.filter(user=request.user)
        username = request.user.username
    else:
        cars = Car.objects.none()
        username = None

    return render(request, 'cars/my_cars.html', {'cars': cars, 'username': username})
