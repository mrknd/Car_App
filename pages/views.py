from django.shortcuts import render

from pages.models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('created_at')
    all_cars = Car.objects.all().order_by('created_at')
    # search_fields = Car.objects.values('model', 'state', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    state_search = Car.objects.values_list('state', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        # 'search_fields': search_fields,
        'model_search': model_search,
        'state_search': state_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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