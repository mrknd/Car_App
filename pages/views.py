from django.shortcuts import render

from pages.models import Team


def home(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
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