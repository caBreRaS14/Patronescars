# cars/views/car_views.py
from django.shortcuts import render, get_object_or_404, redirect
from cars.models import Car
from django.contrib.auth.decorators import login_required
from cars.forms import CarForm

# Listar coches

def list_cars(request):
    # Obtenemos todos los coches
    cars = Car.objects.all()
    
    # Obtener el valor de búsqueda si existe
    query = request.GET.get('q')
    if query:
        cars = cars.filter(brand__icontains=query)
    
    # Si el usuario está autenticado, filtrar por el usuario propietario
    if request.user.is_authenticated:
        username = request.user.username
        
    else:
        
        username = None
    
    return render(request, 'cars/list_cars.html', {'cars': cars, 'username': username})


@login_required
def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)  # No guarda aún en la BD
            car.user = request.user  # Asigna el usuario autenticado
            car.save()  # Guarda el coche en la BD
            return redirect('list_cars')  # Redirige a la lista de coches
    else:
        form = CarForm()
    
    return render(request, 'cars/create_car.html', {'form': form})


# Editar coche

@login_required
def edit_car(request, car_id):
    # Obtén el coche que se quiere editar
    car = get_object_or_404(Car, id=car_id)
    
    # Asegúrate de que el usuario que edita el coche sea el propietario
    if car.user != request.user:
        return redirect('list_cars')  # Redirige si el usuario no es el propietario

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('list_cars')  # Redirige al listado de coches
    else:
        form = CarForm(instance=car)  # Carga el coche en el formulario
    
    return render(request, 'cars/edit_car.html', {'form': form, 'car': car})

# Eliminar coche
@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.user == request.user:
        car.delete()
    return redirect('list_cars')
