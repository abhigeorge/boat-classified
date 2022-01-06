from django.urls import path
from . import views

urlpatterns = [
    path('', views.boats, name='boats'),
    path('<int:id>', views.boat_detail, name='boat_detail'),
    path('search', views.search, name='search'),
]
