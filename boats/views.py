from django.shortcuts import render, get_object_or_404
from .models import Boat
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def boats(request):
    boats = Boat.objects.order_by('-created_date')
    paginator = Paginator(boats, 4)
    page = request.GET.get('page')
    paged_boats = paginator.get_page(page)

    boat_type_search = Boat.objects.values_list('boat_type', flat=True).distinct()
    make_search = Boat.objects.values_list('make', flat=True).distinct()
    model_search = Boat.objects.values_list('model', flat=True).distinct()
    state_search = Boat.objects.values_list('state', flat=True).distinct()
    year_search = Boat.objects.values_list('year', flat=True).distinct()
    tax_status_search = Boat.objects.values_list('tax_status', flat=True).distinct()
    data = {
        'boats': paged_boats,
        'boat_type_search': boat_type_search,
        'make_search': make_search,
        'model_search': model_search,
        'state_search': state_search,
        'year_search': year_search,
        'tax_status_search': tax_status_search,
    }
    return render(request, 'boats/boats.html', data)

def boat_detail(request, id):
    single_boat = get_object_or_404(Boat, pk=id)

    data = {
        'single_boat': single_boat,
    }

    return render(request, 'boats/boat_detail.html', data)

def search(request):
    boats = Boat.objects.order_by('-created_date')

    boat_type_search = Boat.objects.values_list('boat_type', flat=True).distinct()
    make_search = Boat.objects.values_list('make', flat=True).distinct()
    model_search = Boat.objects.values_list('model', flat=True).distinct()
    state_search = Boat.objects.values_list('state', flat=True).distinct()
    year_search = Boat.objects.values_list('year', flat=True).distinct()
    tax_status_search = Boat.objects.values_list('tax_status', flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            boats = boats.filter(boat_description__icontains=keyword)

    if 'boat_type' in request.GET:
        boat_type = request.GET['boat_type']
        if boat_type:
            boats = boats.filter(boat_type__iexact=boat_type)
    
    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            boats = boats.filter(make__iexact=make)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            boats = boats.filter(model__iexact=model)
    
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            boats = boats.filter(state__iexact=state)
    
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            boats = boats.filter(year__iexact=year)

    if 'tax_status' in request.GET:
        tax_status = request.GET['tax_status']
        if tax_status:
            boats = boats.filter(tax_status__iexact=tax_status)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            boats = boats.filter(price__gte=min_price, price__lte=max_price)


    data = {
        'boats': boats,
        'boat_type_search': boat_type_search,
        'make_search': make_search,
        'model_search': model_search,
        'state_search': state_search,
        'year_search': year_search,
        'tax_status_search': tax_status_search,
    }
    return render(request, 'boats/search.html' , data)
