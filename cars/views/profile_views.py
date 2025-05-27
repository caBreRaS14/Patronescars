# cars/views/profile_views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'profile/profile.html')
