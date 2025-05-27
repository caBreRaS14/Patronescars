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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.year}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'car')

    def __str__(self):
        return f"{self.user.username} - {self.car}"
    
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.user.username} en {self.car}"
    
