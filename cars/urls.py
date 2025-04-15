from django.urls import path
from cars.views.auth_views import register, login_view, logout_view
from cars.views.car_views import list_cars, edit_car, delete_car
from django.conf import settings
from django.conf.urls.static import static
from cars.views.just_car import car_detail
from cars.views.my_cars import my_cars
from cars.views.create_car import create_car, get_models_for_brand




urlpatterns = [
    path('cars/', list_cars, name='list_cars'),
    path('create/', create_car, name='create_car'),
    path('edit/<int:car_id>/', edit_car, name='edit_car'),
    path('delete/<int:car_id>/', delete_car, name='delete_car'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', list_cars, name='home'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
    path('my_cars/', my_cars, name='my_cars'),
    path('get_models_for_brand/<str:brand>/', get_models_for_brand, name='get_models_for_brand'),
    

]

if settings.DEBUG:
    
    print("Modo de depuración activado")

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

