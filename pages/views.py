from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = f"You have a new message {subject}"
        message_body = (f"Name {name} . \n"
                        f"Email {email} . \n"
                        f"Phone {phone} . \n"
                        f"Message {message} .")

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            "vatikan98@gmail.com",
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, f'Your message has been sent to')
        return redirect('contact')

    return render(request=request, template_name='pages/contact.html')
