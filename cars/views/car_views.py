# cars/views/car_views.py
from django.shortcuts import render, get_object_or_404, redirect
from cars.models import Car
from django.contrib.auth.decorators import login_required
from cars.forms import CarForm

# Listar coches
def list_cars(request):
    cars = Car.objects.all()

    # Filtro de búsqueda general (opcional)
    query = request.GET.get('q')
    if query:
        cars = cars.filter(brand__icontains=query)

    # Filtros individuales
    selected_brands = request.GET.getlist('brand')  # checkbox puede devolver múltiples
    year = request.GET.get('year')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    description = request.GET.get('description')

    # Filtro por marcas seleccionadas
    if selected_brands:
        cars = cars.filter(brand__in=selected_brands)

    # Filtro por año
    if year:
        cars = cars.filter(year__icontains=year)

    # Filtro por precio mínimo
    if price_min:
        try:
            cars = cars.filter(price__gte=int(price_min))
        except ValueError:
            pass

    # Filtro por precio máximo
    if price_max:
        try:
            cars = cars.filter(price__lte=int(price_max))
        except ValueError:
            pass

    # Filtro por descripción
    if description:
        cars = cars.filter(description__icontains=description)

    username = request.user.username if request.user.is_authenticated else None

    context = {
        'cars': cars,
        'username': username,
        'filters': {
            'brands': selected_brands,
            'year': year or '',
            'price_min': price_min or '',
            'price_max': price_max or '',
            'description': description or ''
        },
        'available_brands': Car.BRAND_CHOICES  # Para renderizar los checkboxes en el HTML
    }

    return render(request, 'cars/list_cars.html', context)




@login_required
def edit_car(request, car_id):
    
    car = get_object_or_404(Car, id=car_id)
    if car.user != request.user:
        return redirect('list_cars')
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('list_cars')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/edit_car.html', {'form': form, 'car': car})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.user == request.user:
        car.delete()
    return redirect('list_cars')
