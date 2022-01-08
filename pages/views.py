from django.shortcuts import render, redirect
from .models import Team
from boats.models import Boat
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_boats = Boat.objects.order_by('-created_date').filter(is_featured=True)
    all_boats = Boat.objects.order_by('-created_date')
    boat_type_search = Boat.objects.values_list('boat_type', flat=True).distinct()
    make_search = Boat.objects.values_list('make', flat=True).distinct()
    model_search = Boat.objects.values_list('model', flat=True).distinct()
    state_search = Boat.objects.values_list('state', flat=True).distinct()
    year_search = Boat.objects.values_list('year', flat=True).distinct()
    tax_status_search = Boat.objects.values_list('tax_status', flat=True).distinct()


    data = {
        'teams': teams,
        'featured_boats': featured_boats,
        'all_boats': all_boats,
        'boat_type_search': boat_type_search,
        'make_search': make_search,
        'model_search': model_search,
        'state_search': state_search,
        'year_search': year_search,
        'tax_status': tax_status_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from BoatSeller website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'django@abhigeorge.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')
