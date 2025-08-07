from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Trip, Note
from django.contrib.auth import logout

# Create your views here.
class HomeView(TemplateView):
    template_name = "trip/index.html"
    

def trip_list(request):
    trips = Trip.objects.all()
    context = {
        "trips": trips
    }
    
    return render(request=request, template_name="trip/trip_list.html", context=context)