from django.shortcuts import render
from .models import golfer, options, round
from django.views.generic import ListView
# Create your views here.
def landing(request):
    return render(request, 'golf_data/landing.html')

class round(ListView):
    model = round
    template = 'golf_data/round.html'