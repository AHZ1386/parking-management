from django.db import models

class Parking(models.Model): 
    hourly_fee = models.IntegerField()
    
    def __str__(self):
        return str(self.pk)
    
    
class Car(models.Model):
    car_plate = models.CharField(max_length=8)
    car_type = models.CharField(max_length=100)
    car_color = models.CharField(max_length=50)
    parking_lot = models.OneToOneField(Parking, on_delete=models.CASCADE, related_name='lot')
    enter_time = models.DateTimeField(auto_now=True)
    exit_time = models.DateTimeField(auto_now=True)
    
