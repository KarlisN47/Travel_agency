from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from travel.models import Trip
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'registration/signup.html', {'form': form})


class BaseView(TemplateView):
    template_name = 'home.html'


class BaseView2(TemplateView):
    template_name = 'index.html'


class DetailTripView(DetailView):
    model = Trip
    template_name = 'detail.html'
    context_object_name = 'trip'


class TripListView(ListView):
    model = Trip
    template_name = 'list/global.html'
    context_object_name = 'trips'


class EuropeTripView(ListView):
    model = Trip
    template_name = 'list/continent/europe.html'
    context_object_name = 'trips'


class TrippListView(ListView):
    model = Trip
    template_name = 'list.html'
    context_object_name = 'trips'

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', None)
        trip = self.request.GET.get('trip', 'id')

        new_queryset = Trip.objects.order_by(trip)

        if filter_val:
            new_queryset = new_queryset.filter(airport__city__country__name=filter_val) | \
                           new_queryset.filter(airport__city__country__continent__name=filter_val) | \
                           new_queryset.filter(airport__city__name=filter_val) | \
                           new_queryset.filter(airport__city__country__continent__globally__name=filter_val)

        return new_queryset

    def get_context_data(self, **kwargs):
        context = super(TrippListView, self).get_context_data(**kwargs)

        context['trip'] = self.request.GET.get(
            'trip', 'id')

        context['filter'] = self.request.GET.get(
            'filter', None)

        return context
