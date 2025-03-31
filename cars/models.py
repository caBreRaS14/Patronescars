from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    BRAND_CHOICES = [
        ('Tesla', 'Tesla'),
        ('Nissan', 'Nissan'),
        ('BMW', 'BMW'),
        ('Audi', 'Audi'),
        ('Hyundai', 'Hyundai'),
        ('Kia', 'Kia'),
        ('Otros', 'Otros'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)  # Marca del coche
    model = models.CharField(max_length=100)  # Modelo del coche
    year = models.PositiveIntegerField()  # Año de fabricación
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del coche
    description = models.TextField()  # Descripción del coche
    image = models.ImageField(upload_to='cars/', blank=True, null=True)  # Imagen del coche (opcional)
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de publicación

    def __str__(self):
        return f"{self.brand} {self.model} - {self.year}"
