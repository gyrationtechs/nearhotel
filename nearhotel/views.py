from django.shortcuts import render
from ggcode.models import Booking

def home(request):
    return render(request, 'home.html')


