from django import forms
from django.contrib.auth.models import User
from .models import Car


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmar contraseña")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Las contraseñas no coinciden.")

class CarForm(forms.ModelForm):
    model = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'multiple': 'multiple', 'style': 'color: black;'}),
        choices=[],  # Se llenan dinámicamente
    )

    class Meta:
        model = Car  # ✅ Aquí va el modelo, no un campo de formulario
        fields = ['brand', 'model', 'year', 'price', 'description', 'image',
                  'location', 'traction_control', 'kilometers', 'body_type',
                  'fuel_type', 'doors', 'transmission', 'steering', 'plate']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Asignar las opciones de marca
        self.fields['brand'].choices = Car.BRAND_CHOICES

        # Obtener marca seleccionada
        brand = None
        if self.data.get('brand'):
            brand = self.data.get('brand')  # cuando se envía desde el formulario
        elif self.instance and self.instance.brand:
            brand = self.instance.brand  # cuando se edita una instancia

        if brand:
            self.fields['model'].choices = [(m, m) for m in self.get_models_for_brand(brand)]
        else:
            self.fields['model'].choices = []

    def get_models_for_brand(self, brand):
        models = {
            'Renault': Car.RENAULT_MODELS,
            'Toyota': Car.TOYOTA_MODELS,
            'Chevrolet': Car.CHEVROLET_MODELS,
            'Mazda': Car.MAZDA_MODELS,
            'Kia': Car.KIA_MODELS,
            'Hyundai': Car.HYUNDAI_MODELS,
            'Nissan': Car.NISSAN_MODELS,
            'Suzuki': Car.SUZUKI_MODELS,
            'Volkswagen': Car.VOLKSWAGEN_MODELS,
            'Ford': Car.FORD_MODELS,
            'BMW': Car.BMW_MODELS,
            'Audi': Car.AUDI_MODELS,
            'Tesla': Car.TESLA_MODELS,
            'Mini': Car.MINI_MODELS,
            'BYD': Car.BYD_MODELS,
            'Zhidou': Car.ZHIDOU_MODELS,
            'Otros': Car.OTHER_MODELS,
        }
        return models.get(brand, [])
