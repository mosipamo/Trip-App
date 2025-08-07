from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from .models import Trip, Note
from django.contrib.auth import logout
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = "trip/index.html"
    

def trip_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        "trips": trips
    }
    
    return render(request=request, template_name="trip/trip_list.html", context=context)

class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ["city", "country", "start_date", "end_date"]
    # template named model_form.html
    
    def form_valid(self, form): # run this when form is to be submitted
        # owner filed = logged in user
        form.instance.owner = self.request.user        
        
        return super().form_valid(form)