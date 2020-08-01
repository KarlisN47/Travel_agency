from django.urls import path
from travel.views import BaseView
from . import views
urlpatterns = [
    path('', BaseView.as_view(), name='home')
]