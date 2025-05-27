from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from cars.models import Car, Favorite

@login_required
def toggle_favorite(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, car=car)
    
    if not created:
        favorite.delete()
    return redirect('car_detail', car_id=car.id)  # Asegúrate de tener esta vista o cambia el redirect

@login_required
def user_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('car')
    return render(request, 'cars/user_favorites.html', {'favorites': favorites})


@login_required
def my_favorites_view(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('car')
    return render(request, 'cars/user_favorites.html', {'favorites': favorites})