from django.shortcuts import render, get_object_or_404
from cars.models import Car

def car_detail(request, car_id):
    # Obtener el coche por su ID, si no existe, retorna un error 404
    car = get_object_or_404(Car, id=car_id)

    # Renderiza la plantilla con los detalles del coche
    return render(request, 'cars/car_detail.html', {'car': car})
