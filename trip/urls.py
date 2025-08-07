from django.urls import path
from .views import HomeView, trip_list, TripCreateView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', trip_list, name="trip-list"),
    path('dashboard/trip/create/', TripCreateView.as_view(), name="trip-create"),
]