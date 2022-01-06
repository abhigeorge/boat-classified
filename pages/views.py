from django.shortcuts import render
from .models import Team
from boats.models import Boat

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
    return render(request, 'pages/contact.html')
