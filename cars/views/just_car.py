from django.shortcuts import render, get_object_or_404, redirect
from cars.models import Car
from cars.forms import CommentForm

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    comments = car.comments.select_related('user').order_by('-created_at')
    
    print(comments)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.car = car
            comment.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = CommentForm()

    return render(request, 'cars/car_detail.html', {
        'car': car,
        'comments': comments,
        'form': form
    })