from django.shortcuts import render

from pages.models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('created_at')
    all_cars = Car.objects.all().order_by('created_at')
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request=request, template_name='pages/home.html', context=context)


def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request=request, template_name='pages/about.html', context=context)


def services(request):
    return render(request=request, template_name='pages/services.html')


def contact(request):
    return render(request=request, template_name='pages/contact.html')