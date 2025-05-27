from django.urls import path
from cars.views.auth_views import register, login_view, logout_view
from cars.views.car_views import list_cars, create_car, edit_car, delete_car
from django.conf import settings
from django.conf.urls.static import static
from cars.views.just_car import car_detail
from cars.views.profile_views import profile
from cars.views.my_cars import my_cars
from cars.views.politocas import pqrs
from cars.views.favorite_views import my_favorites_view, user_favorites, toggle_favorite



urlpatterns = [
    path('cars/', list_cars, name='list_cars'),
    path('create/', create_car, name='create_car'),
    path('edit/<int:car_id>/', edit_car, name='edit_car'),
    path('delete/<int:car_id>/', delete_car, name='delete_car'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('', list_cars, name='home'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
    path('my_cars/', my_cars, name='my_cars'),
    path('pqr/', pqrs, name='pqr'),
    path('favorito/<int:car_id>/', toggle_favorite, name='toggle_favorite'),
    path('mis-favoritos/', user_favorites, name='user_favorites'),
    path('favorites/', my_favorites_view, name='my_favorites'),
    

]

if settings.DEBUG:
    # Código relacionado con la configuración de DEBUG
    print("Modo de depuración activado")

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

