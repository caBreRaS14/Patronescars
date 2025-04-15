from django.shortcuts import render, get_object_or_404
from cars.models import Car

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/car_detail.html', {'car': car})
