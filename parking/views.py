from django.shortcuts import render
from .models import Car, Parking
from .forms import AddCarToParkingForm
from django.http import HttpResponse


def add_car_to_parking(request):
    if request.method == 'POST':
        form = AddCarToParkingForm(request.POST)
        if form.is_valid():
            # ذخیره کردن ماشین جدید
            form.save()
            # به صفحه موفقیت یا لیست ماشین‌ها بروید
            return HttpResponse('some_success_url')
    else:
        form = AddCarToParkingForm()

    return render(request, 'add_car.html', {'form': form})

def index(reqeust):
    context = {
        'parking_lot': Parking.objects.all(),
        # 'form': form
    }
    return render(reqeust, "add_car.html", context)
