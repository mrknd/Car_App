from django.shortcuts import render


def cars(request):
    return render(request=request, template_name='cars/cars.html')
