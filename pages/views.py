from django.shortcuts import render


def home(request):
    return render(request=request, template_name='pages/home.html')


def about(request):
    return render(request=request, template_name='pages/about.html')


def services(request):
    return render(request=request, template_name='pages/services.html')


def contact(request):
    return render(request=request, template_name='pages/contact.html')