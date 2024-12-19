from django import forms
from .models import Car,Parking

class AddCarToParkingForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_plate', 'car_type', 'car_color',
                  'parking_lot', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        used_parkings = Car.objects.values_list('parking_lot', flat=True)
        self.fields['parking_lot'].queryset = Parking.objects.exclude(id__in=used_parkings)
