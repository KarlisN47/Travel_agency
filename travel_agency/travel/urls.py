from django.urls import path
from travel.views import BaseView, BaseView2, DetailTripView, TripListView, EuropeTripView, TrippListView, signup_view
from . import views
urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('index/', BaseView2.as_view(), name='index'),
    path('detail/<int:pk>', DetailTripView.as_view(), name='detail'),
    path('global/', TripListView.as_view(), name='global'),
    path('europe/', EuropeTripView.as_view(), name='europe'),
    path('list/', TrippListView.as_view(), name='list'),
    path('signup/', signup_view, name="signup"),
]