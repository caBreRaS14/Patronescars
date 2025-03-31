from django.shortcuts import render
from cars.models import Car

def my_cars(request):
    # Solo obtenemos los coches creados por el usuario autenticado
    if request.user.is_authenticated:
        cars = Car.objects.filter(user=request.user)
        username = request.user.username  # Obtener el nombre de usuario
    else:
        cars = Car.objects.none()  # Si no está autenticado, no mostrar coches
        username = None  # No hay nombre de usuario

    return render(request, 'cars/my_cars.html', {'cars': cars, 'username': username})
