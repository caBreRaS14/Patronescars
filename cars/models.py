from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Car(models.Model):
    BRAND_CHOICES = [
        ('Renault', 'Renault'),
        ('Toyota', 'Toyota'),
        ('Chevrolet', 'Chevrolet'),
        ('Mazda', 'Mazda'),
        ('Kia', 'Kia'),
        ('Hyundai', 'Hyundai'),
        ('Nissan', 'Nissan'),
        ('Suzuki', 'Suzuki'),
        ('Volkswagen', 'Volkswagen'),
        ('Ford', 'Ford'),
        ('BYD', 'BYD'),
        ('Zhidou', 'Zhidou'),
        ('Mini', 'Mini'),
        ('BMW', 'BMW'),
        ('Tesla', 'Tesla'),
        ('Audi', 'Audi'),
        ('Otros', 'Otros'),
    ]
    
    SUZUKI_MODELS = [
        ('Swift', 'Swift'),
        ('Vitara', 'Vitara'),
        ('S-Cross', 'S-Cross'),
        ('Baleno', 'Baleno'),
        ('Celerio', 'Celerio'),
        ('Jimny', 'Jimny'),
        ('Ignis', 'Ignis'),
        ('SX4', 'SX4'),
    ]

    
    VOLKSWAGEN_MODELS = [
        ('Golf', 'Golf'),
        ('Jetta', 'Jetta'),
        ('Tiguan', 'Tiguan'),
        ('Passat', 'Passat'),
        ('Polo', 'Polo'),
        ('Touareg', 'Touareg'),
        ('Virtus', 'Virtus'),
        ('Up', 'Up'),
    ]
    
    BYD_MODELS = [
        ('Tang', 'Tang'),
        ('Qin', 'Qin'),
        ('Song', 'Song'),
        ('Yuan', 'Yuan'),
        ('Atto 3', 'Atto 3'),  # Eléctrico
    ]
    
    ZHIDOU_MODELS = [
        ('D2', 'D2'),  # Eléctrico
    ]
    
    MINI_MODELS = [
        ('Cooper', 'Cooper'),
        ('Countryman', 'Countryman'),
        ('Clubman', 'Clubman'),
    ]
    
    TESLA_MODELS = [
        ('Model S', 'Model S'),
        ('Model 3', 'Model 3'),
        ('Model X', 'Model X'),
        ('Model Y', 'Model Y'),
    ]




    
    JEEP_MODELS = [
        ('Cherokee', 'Cherokee'),
        ('Wrangler', 'Wrangler'),
        ('Renegade', 'Renegade'),
        ('Grand Cherokee', 'Grand Cherokee'),
        ('Compass', 'Compass'),
    ]

    
    MERCEDES_MODELS = [
        ('Clase A', 'Clase A'),
        ('Clase C', 'Clase C'),
        ('Clase E', 'Clase E'),
        ('Clase S', 'Clase S'),
        ('GLA', 'GLA'),
        ('GLC', 'GLC'),
        ('GLS', 'GLS'),
        ('CLA', 'CLA'),
        ('AMG GT', 'AMG GT'),
    ]

    
    PEUGEOT_MODELS = [
        ('208', '208'),
        ('2008', '2008'),
        ('3008', '3008'),
        ('5008', '5008'),
        ('308', '308'),
    ]

    
    CHERY_MODELS = [
        ('Tiggo 2', 'Tiggo 2'),
        ('Tiggo 3', 'Tiggo 3'),
        ('Tiggo 4', 'Tiggo 4'),
        ('Tiggo 5', 'Tiggo 5'),
    ]

    
    HONDA_MODELS = [
        ('Civic', 'Civic'),
        ('CR-V', 'CR-V'),
        ('Fit', 'Fit'),
        ('HR-V', 'HR-V'),
        ('Pilot', 'Pilot'),
        ('Accord', 'Accord'),
        ('CRV Hybrid', 'CRV Hybrid'),
    ]

    
    FORD_MODELS = [
        ('Focus', 'Focus'),
        ('Escape', 'Escape'),
        ('Explorer', 'Explorer'),
        ('Mustang', 'Mustang'),
        ('Ranger', 'Ranger'),
        ('F-150', 'F-150'),
        ('Fiesta', 'Fiesta'),
        ('Mondeo', 'Mondeo'),
    ]

    
    KIA_MODELS = [
        ('Sportage', 'Sportage'),
        ('Seltos', 'Seltos'),
        ('Picanto', 'Picanto'),
        ('Rio', 'Rio'),
        ('K900', 'K900'),
        ('Carnival', 'Carnival'),
        ('Optima', 'Optima'),
        ('Soul', 'Soul'),
    ]

    
    AUDI_MODELS = [
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('A5', 'A5'),
        ('A6', 'A6'),
        ('Q5', 'Q5'),
        ('Q7', 'Q7'),
        ('Q8', 'Q8'),
        ('A8', 'A8'),
        ('TT', 'TT'),
        ('R8', 'R8'),
    ]
    
    OTHER_MODELS = [
        ('Otros', 'Otros'),
    ]


    
    BMW_MODELS = [
        ('Series 3', 'Series 3'),
        ('X5', 'X5'),
        ('X3', 'X3'),
        ('Series 5', 'Series 5'),
        ('Series 7', 'Series 7'),
        ('M3', 'M3'),
        ('X1', 'X1'),
        ('X6', 'X6'),
        ('Series 4', 'Series 4'),
        ('i3', 'i3'),  # Eléctrico
        ('i8', 'i8'),  # Eléctrico
    ]

    
    HYUNDAI_MODELS = [
        ('Tucson', 'Tucson'),
        ('Kona', 'Kona'),
        ('Elantra', 'Elantra'),
        ('Santa Fe', 'Santa Fe'),
        ('Creta', 'Creta'),
        ('i10', 'i10'),
        ('i20', 'i20'),
        ('Sonata', 'Sonata'),
        ('Palisade', 'Palisade'),
    ]

    
    MAZDA_MODELS = [
        ('Mazda 3', 'Mazda 3'),
        ('Mazda CX-5', 'Mazda CX-5'),
        ('Mazda CX-3', 'Mazda CX-3'),
        ('Mazda 6', 'Mazda 6'),
        ('Mazda CX-50', 'Mazda CX-50'),
        ('Mazda MX-5', 'Mazda MX-5'),
        ('Mazda 2', 'Mazda 2'),
    ]

    
    NISSAN_MODELS = [
        ('Versa', 'Versa'),
        ('X-Trail', 'X-Trail'),
        ('Frontier', 'Frontier'),
        ('March', 'March'),
        ('Sentra', 'Sentra'),
        ('Pathfinder', 'Pathfinder'),
        ('Qashqai', 'Qashqai'),
        ('Juke', 'Juke'),
        ('Altima', 'Altima'),
        ('Murano', 'Murano'),
    ]

    
    CHEVROLET_MODELS = [
        ('Spark', 'Spark'),
        ('Aveo', 'Aveo'),
        ('Tracker', 'Tracker'),
        ('Sail', 'Sail'),
        ('Camaro', 'Camaro'),
        ('Taho', 'Taho'),
        ('Equinox', 'Equinox'),
        ('Colorado', 'Colorado'),
        ('Cruze', 'Cruze'),
        ('Onix', 'Onix'),
        ('Blazer', 'Blazer'),
        ('Suburban', 'Suburban'),
        ('Trailblazer', 'Trailblazer'),
        ('Captiva', 'Captiva'),
        ('Spin', 'Spin'),
    ]

    
    RENAULT_MODELS = [
        ('Duster', 'Duster'),
        ('Stepway', 'Stepway'),
        ('Sandero', 'Sandero'),
        ('Logan', 'Logan'),
        ('Kwid', 'Kwid'),
        ('Captur', 'Captur'),
        ('Oroch', 'Oroch'),
        ('Koleos', 'Koleos'),
        ('ZOE', 'ZOE'),  # eléctrico
        ('Twizy', 'Twizy'),  # eléctrico urbano
    ]
    
    TOYOTA_MODELS = [
        ('Corolla', 'Corolla'),
        ('Corolla Cross', 'Corolla Cross'),
        ('Hilux', 'Hilux'),
        ('Fortuner', 'Fortuner'),
        ('Yaris', 'Yaris'),
        ('Prado', 'Prado'),
        ('Land Cruiser', 'Land Cruiser'),
        ('RAV4', 'RAV4'),
        ('Raize', 'Raize'),
        ('SW4', 'SW4'),
        ('Camry', 'Camry'),
        ('Tacoma', 'Tacoma'),
        ('4Runner', '4Runner'),
        ('C-HR', 'C-HR'),
        ('Prius', 'Prius'),  # Híbrido
        ('bZ4X', 'bZ4X'),  # Eléctrico
        ('Sienna', 'Sienna'),
        ('Vios', 'Vios'),
        ('Auris', 'Auris'),
        ('Supra', 'Supra'),
        ('Avanza', 'Avanza'),
        ('Innova', 'Innova'),
        ('Etios', 'Etios'),
    ]


    BODY_CHOICES = [
        ('Sedán', 'Sedán'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
        ('Pickup', 'Pickup'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Otro', 'Otro'),
    ]

    FUEL_CHOICES = [
        ('Eléctrico', 'Eléctrico'),
        ('Gasolina', 'Gasolina'),
        ('Diesel', 'Diesel'),
        ('Híbrido', 'Híbrido'),
    ]

    TRANSMISSION_CHOICES = [
        ('Automática', 'Automática'),
        ('Manual', 'Manual'),
    ]

    DIRECTION_CHOICES = [
        ('Hidráulica', 'Hidráulica'),
        ('Eléctrica', 'Eléctrica'),
        ('Mecánica', 'Mecánica'),
    ]

    TRACTION_CHOICES = [
        ('Delantera', 'Delantera'),
        ('Trasera', 'Trasera'),
        ('4x4', '4x4'),
        ('AWD', 'AWD'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, default='Otros')
    model = models.CharField(max_length=50, default='Otros')
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(2010), MaxValueValidator(2026)],
        default=2020
    )
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    location = models.CharField(max_length=100, verbose_name="Lugar de publicación", default="Sin especificar")
    traction_control = models.CharField(
        max_length=20,
        choices=TRACTION_CHOICES,
        verbose_name="Control de tracción",
        default='Delantera'
    )
    kilometers = models.PositiveIntegerField(verbose_name="Kilómetros", default=0)
    body_type = models.CharField(
        max_length=20,
        choices=BODY_CHOICES,
        verbose_name="Tipo de carrocería",
        default='SUV'
    )
    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES,
        verbose_name="Tipo de combustible",
        default='Eléctrico'
    )
    doors = models.PositiveIntegerField(verbose_name="Puertas", default=4)
    transmission = models.CharField(
        max_length=20,
        choices=TRANSMISSION_CHOICES,
        verbose_name="Transmisión",
        default='Automática'
    )
    steering = models.CharField(
        max_length=20,
        choices=DIRECTION_CHOICES,
        verbose_name="Dirección",
        default='Eléctrica'
    )
    plate = models.CharField(
        max_length=6,
        verbose_name="Placa",
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{3}\d{3}$',
                message="La placa debe tener el formato ABC123 (3 letras + 3 números)"
            )
        ],
        default='AAA000'
    )

    def __str__(self):
        return f"{self.brand} {self.model} - {self.year}"
