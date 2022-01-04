from django.shortcuts import render

# Create your views here.
def boats(request):
    return render(request, 'boats/boats.html')
