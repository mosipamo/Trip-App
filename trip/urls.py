from django.urls import path
from .views import HomeView, trip_list

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', trip_list, name="trip-list"),
]

"""
    accounts/login/ [name='login']
    accounts/logout/ [name='logout']
    accounts/password_change/ [name='password_change']
    accounts/password_change/done/ [name='password_change_done']
    accounts/password_reset/ [name='password_reset']
    accounts/password_reset/done/ [name='password_reset_done']
    accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    accounts/reset/done/ [name='password_reset_complete']
"""