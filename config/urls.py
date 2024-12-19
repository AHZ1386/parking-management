from django.contrib import admin
from django.urls import path
from parking.views import add_car_to_parking,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-car', add_car_to_parking, name='add_car'),
    path('', index, name='index'),

]
