from django.urls import path
from . import views

urlpatterns = [
    path('', views.boats, name='boats'),
]
