# cars/views/auth_views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

# Registrar nuevo usuario
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'cars/register.html', {'form': form})

# Iniciar sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigir a la página principal
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, 'cars/login.html')

# Cerrar sesión
def logout_view(request):
    logout(request)
    return redirect('home')
