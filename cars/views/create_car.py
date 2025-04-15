from django.shortcuts import render, redirect
from cars.models import Car
from django.contrib.auth.decorators import login_required
from cars.forms import CarForm
from django.http import JsonResponse


@login_required
def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.model = form.cleaned_data['model']  # Es lista → válido para JSONField
            car.save()
            return redirect('success')
    else:
        form = CarForm()

    return render(request, 'cars/create_car.html', {'form': form})




def get_models_for_brand(request, brand):
    model_list = CarForm().get_models_for_brand(brand)
    return JsonResponse({'models': model_list})
