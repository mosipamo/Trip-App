from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Trip, Note

# Create your views here.
class HomeView(TemplateView):
    template_name = "trip/index.html"
    

def trips_list(request):
    trips = Trip.objects.all()
    context = {
        "trips": trips
    }
    
    return render(request=request, template_name="trip/trips_list.html", context=context)